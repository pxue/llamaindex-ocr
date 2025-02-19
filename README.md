# pdf table data parser

1. [Marker](https://github.com/VikParuchuri/marker)

Marker is a OCR + LLM lib with propietary table transformer

![llm score](https://pbs.twimg.com/media/GkKzZdzXAAAxG6y?format=jpg&name=large)

some key features:

- llm mode that augments marker with models like gemini flash
- improved math, w/inline math
- links and references
- better tables and forms

LLM mode iterates on marker output for certain blocks. You can use gemini, or
local models via ollama. More models coming soon.

Marker + llms is faster and hallucination-free vs using llms alone. Here marker
+ gemini flash beats gemini flash alone on a fintabnet benchmark.

![marker
+ gemini](https://pbs.twimg.com/media/GkKzzzbWYAERp56?format=jpg&name=small)


Table improvements are:
- new table recognition model
- table merging across pages
- math and formatting inside tables
- output in html, markdown, or json

![table](https://pbs.twimg.com/media/GkKz93rXYAANca4?format=jpg&name=4096x4096)

Up next is:

- More formats (docx, pptx, xlsx, etc)
- Improved layout detection on scientific papers, engineering documents, newspapers
- Structured data extraction

2. llamaindex / llamaparse

It is really good at the following:

✅ Broad file type support: Parsing a variety of unstructured file types (.pdf, .pptx, .docx, .xlsx, .html) with text, tables, visual elements, weird layouts, and more.
✅ Table recognition: Parsing embedded tables accurately into text and semi-structured representations.
✅ Multimodal parsing and chunking: Extracting visual elements (images/diagrams) into structured formats and return image chunks using the latest multimodal models.
✅ Custom parsing: Input custom prompt instructions to customize the output the way you want it.

Overall more easily integrated into LLAMAIndex if needed.
