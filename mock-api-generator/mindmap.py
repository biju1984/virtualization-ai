from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def dict_to_opml(parent, dict_item):
    if isinstance(dict_item, dict):
        for k, v in dict_item.items():
            node = SubElement(parent, "outline", {"text": k})
            dict_to_opml(node, v)
    elif isinstance(dict_item, list):
        for item in dict_item:
            node = SubElement(parent, "outline", {"text": item})
    else:
        node = SubElement(parent, "outline", {"text": str(dict_item)})

root = Element("opml", {"version": "2.0"})
head = SubElement(root, "head")
title = SubElement(head, "title")
title.text = "API Mockup Tool Mind Map"
body = SubElement(root, "body")

mind_map = {
    "User Interaction for API Mockup Tool": {
        "Welcome Screen": {
            "Display Welcome Message": None,
            "Explain Tool Capabilities": None,
            "Options": ["Create New API", "Modify Existing API"],
            "Provide Tutorial/Guided Tour": None
        },
        "Starting a New API": {
            "Choose Input Method": {
                "Text Prompt": {
                    "Enter High-Level Description": None,
                    "Example": "Fetch user details by user ID"
                },
                "File Upload": {
                    "Upload OpenAPI Spec, JSON, or YAML": None,
                    "Parse File and Display Summary": None
                }
            }
        },
        "Processing Initial Input": {
            "Text Prompt Handling": {
                "Use OpenAI for Initial Specification": None,
                "Example OpenAI Prompt": None,
                "Receive and Parse Response": None,
                "Validate Response": None
            },
            "File Upload Handling": {
                "Parse Uploaded File": None,
                "Generate Preliminary Specification": None,
                "Validate Parsed Content": None
            }
        },
        "Clarifying Requirements": {
            "Identifying Gaps and Ambiguities": {
                "Analyze Initial Specification": None,
                "Generate Follow-up Questions": None
            },
            "Examples of Follow-up Questions": [
                "What details about the user?",
                "Include query parameters/headers?",
                "Sample request/response?"
            ],
            "Predefined Options for Attributes": {
                "Common Attributes": None,
                "User Selection": None
            }
        },
        "Iterative Refinement": {
            "Iterative Process": {
                "Series of Questions": None,
                "User Answers": None,
                "Update Specification": None
            },
            "Display Updated Specification": None,
            "Iteration Limit": None
        },
        "Handling Different User Scenarios": {
            "Technical User": {
                "Upload Detailed OpenAPI Spec": None,
                "Identify Enhancements": None,
                "Add Endpoints/Parameters/Responses": None,
                "Manual Specification Editing": None
            },
            "Non-Technical User": {
                "Provide High-Level Description": None,
                "Generate Basic Specification": None,
                "Simple, Guided Questions": None,
                "Examples and Templates": None,
                "Select Predefined Attributes/Endpoints": None
            }
        },
        "Error Handling and Validation": {
            "Input Validation": {
                "Validate User Inputs": None,
                "Provide Feedback": None,
                "Request Corrections": None
            },
            "Response Validation": {
                "Validate OpenAI Responses": None,
                "Handle Malformed/Incomplete Responses": None
            },
            "Error Messages and Recovery": {
                "Clear Error Messages": None,
                "Recovery Options": None,
                "Retry Process": None
            }
        },
        "Confirming and Saving Specification": {
            "Review and Confirmation": {
                "Display Final Specification": None,
                "Highlight Changes/Additions": None,
                "User Confirmation/Modification": None,
                "Save with Version Number": None
            },
            "Version Control": {
                "Save to Database": None,
                "Track Changes": None,
                "Revert to Previous Versions": None
            }
        }
    }
}

dict_to_opml(body, mind_map)

opml_output_path = "API_Mockup_Tool_Mind_Map.opml"
tree = ElementTree(root)
tree.write(opml_output_path, encoding="utf-8", xml_declaration=True)

opml_output_path
