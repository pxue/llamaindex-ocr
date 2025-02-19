# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_cloud_services import LlamaParse
from llama_cloud_services.parse.base import ResultType
from llama_index.core.async_utils import asyncio_run, run_jobs
from llama_index.core import SimpleDirectoryReader
import os
import requests
from typing import Optional, Union
from enum import Enum

rr1Schema = """
{
	"$schema": "https://json-schema.org/draft/2020-12/schema",
    
    "type": "object",
    "properties": {
        "property_id": {"type": "string"},
        "building_id": {"type": "string"},
        "unit_id": {"type": "string"},
        "primary_resident": {"type": "string"},
        "unit_type": {"type": "string"},
        "legacy_unit_type": {"type": "string"},
        "unit_amenities_description": {"type": "string"},
        "square_footage": {"type": "number"},
        "lease_status": {"type": "string"},
        "unit_status": {"type": "string"},
        "leased_rent": {"type": "number"},
        "total_concession": {"type": "number"},
        "effective_rent": {"type": "number"},
        "all_other_recurring_fees": {"type": "number"},
        "move_in_date": {"type": "string", "format": "date"},
        "lease_term": {"type": "integer"},
        "apply_date": {"type": "string", "format": "date"},
        "lease_begin_date": {"type": "string", "format": "date"},
        "lease_end_date": {"type": "string", "format": "date"},
        "is_affordable": {"type": "boolean"},
        "is_associate": {"type": "boolean"},
        "is_corporate": {"type": "boolean"},
        "furnished": {"type": "boolean"}
    },
    "required": ["property_id", "unit_id"]
}
"""
# set up parser
parser = LlamaParse(
    result_type=ResultType.JSON,
    use_vendor_multimodal_model=True,
    vendor_multimodal_model_name="gemini-2.0-flash-001",
    structured_output=True,
    structured_output_json_schema_name=rr1Schema
)

# use SimpleDirectoryReader to parse our file
# file_extractor = {".pdf": parser}
# documents = SimpleDirectoryReader(input_files=['input/rr1.pdf'], file_extractor=file_extractor).load_data()

# documents = parser.load_data('input/rr1.pdf')



# with open('output/rr1.json', 'w') as f:
#     f.write(documents[0].get_content())

class ResultType(str, Enum):
    MARKDOWN = "markdown"
    JSON = "json"
    TEXT = "text"
    XLSX = "xlsx"
    PDF = "pdf"
    STRUCTURED = "structured"

def fetch_job_results(job_id: str, result_type: Union[ResultType, str] = ResultType.MARKDOWN) -> Optional[str]:
    """
    Fetch job results from Llama Cloud API.
    
    Args:
        job_id (str): The ID of the job to fetch results for
        result_type (Union[ResultType, str]): The type of result to fetch. 
            Can be 'markdown', 'json', 'text', 'xlsx', 'pdf', or 'structured'
        
    Returns:
        Optional[str]: The result if successful, None if failed
        
    Raises:
        requests.RequestException: If the API request fails
        ValueError: If result_type is invalid
    """
    api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    if not api_key:
        raise ValueError("LLAMA_CLOUD_API_KEY environment variable not set")

    # Convert string to enum if needed
    if isinstance(result_type, str):
        try:
            result_type = ResultType(result_type.lower())
        except ValueError:
            valid_types = ", ".join([t.value for t in ResultType])
            raise ValueError(f"Invalid result_type. Must be one of: {valid_types}")

    url = f"https://api.cloud.llamaindex.ai/api/parsing/job/{job_id}/result/{result_type.value}"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching job results: {e}")
        return None

print(fetch_job_results('ce12684f-16d9-468b-970e-a3b71cd4850e', ResultType.JSON))