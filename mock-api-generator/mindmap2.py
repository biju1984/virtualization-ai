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
            "Display Welcome Message": "A warm and friendly welcome message to introduce users to the tool.",
            "Explain Tool Capabilities": "Briefly explain the capabilities and features of the tool.",
            "Options": {
                "Create New API": "Option to start creating a new API specification from scratch.",
                "Modify Existing API": "Option to edit or refine an existing API specification."
            },
            "Provide Tutorial/Guided Tour": "Offer a guided tour for first-time users to familiarize them with the tool."
        },
        "Starting a New API": {
            "Choose Input Method": {
                "Text Prompt": {
                    "Enter High-Level Description": "Allow users to enter a high-level description of the API they need.",
                    "Example": "For example, 'Fetch user details by user ID'."
                },
                "File Upload": {
                    "Upload OpenAPI Spec, JSON, or YAML": "Allow users to upload an existing specification in OpenAPI, JSON, or YAML format.",
                    "Parse File and Display Summary": "Parse the uploaded file and display a summary of the specification."
                }
            }
        },
        "Processing Initial Input": {
            "Text Prompt Handling": {
                "Use OpenAI for Initial Specification": "Use OpenAI to generate an initial API specification based on the text prompt.",
                "Example OpenAI Prompt": "Example: 'Generate an API specification for fetching user details by user ID.'",
                "Receive and Parse Response": "Receive the response from OpenAI and parse it to create an initial API specification.",
                "Validate Response": "Ensure the response is in the correct format and meets the required standards."
            },
            "File Upload Handling": {
                "Parse Uploaded File": "Parse the uploaded OpenAPI spec, JSON, or YAML file.",
                "Generate Preliminary Specification": "Generate a preliminary API specification based on the parsed content.",
                "Validate Parsed Content": "Ensure the parsed content meets the required standards."
            }
        },
        "Clarifying Requirements": {
            "Identifying Gaps and Ambiguities": {
                "Analyze Initial Specification": "Analyze the initial API specification to identify any missing or unclear details.",
                "Generate Follow-up Questions": "Generate follow-up questions to gather the required information."
            },
            "Examples of Follow-up Questions": [
                "What details do you need about the user?",
                "Do you want to include any query parameters or headers?",
                "Can you provide a sample request and response?"
            ],
            "Predefined Options for Attributes": {
                "Common Attributes": "Provide predefined options for common attributes (e.g., string, integer, boolean).",
                "User Selection": "Allow users to select from these options to simplify the process."
            }
        },
        "Iterative Refinement": {
            "Iterative Process": {
                "Series of Questions": "Ask a series of questions based on the current state of the specification.",
                "User Answers": "User provides answers to the questions.",
                "Update Specification": "Update the specification accordingly."
            },
            "Display Updated Specification": "Display the updated specification after each round of questions.",
            "Iteration Limit": "Implement a configurable limit on the number of iterations to prevent infinite loops."
        },
        "Handling Different User Scenarios": {
            "Technical User": {
                "Upload Detailed OpenAPI Spec": "Allow technical users to upload a comprehensive specification file.",
                "Identify Enhancements": "Identify potential enhancements based on the uploaded file.",
                "Add Endpoints/Parameters/Responses": "Ask the user if they want to add more endpoints, parameters, or response types.",
                "Manual Specification Editing": "Provide options to manually edit the specification."
            },
            "Non-Technical User": {
                "Provide High-Level Description": "Allow non-technical users to provide a general description of the API.",
                "Generate Basic Specification": "Generate a basic specification using OpenAI.",
                "Simple, Guided Questions": "Ask simple, guided questions to refine the specification.",
                "Examples and Templates": "Provide examples and templates for common API patterns.",
                "Select Predefined Attributes/Endpoints": "Allow the user to select from predefined attributes and endpoints."
            }
        },
        "Error Handling and Validation": {
            "Input Validation": {
                "Validate User Inputs": "Validate user inputs (text prompts and file uploads) to ensure they are in the correct format.",
                "Provide Feedback": "Provide feedback and request corrections if needed.",
                "Request Corrections": "Allow users to correct their inputs."
            },
            "Response Validation": {
                "Validate OpenAI Responses": "Validate OpenAI responses to ensure they are complete and correctly formatted.",
                "Handle Malformed/Incomplete Responses": "Handle cases where the response is malformed or incomplete."
            },
            "Error Messages and Recovery": {
                "Clear Error Messages": "Provide clear and informative error messages to the user.",
                "Recovery Options": "Offer options to recover from errors and continue the process.",
                "Retry Process": "Allow users to retry the process if an error occurs."
            }
        },
        "Confirming and Saving Specification": {
            "Review and Confirmation": {
                "Display Final Specification": "Display the final API specification for user review.",
                "Highlight Changes/Additions": "Highlight changes and new additions.",
                "User Confirmation/Modification": "Ask the user to confirm or make further modifications.",
                "Save with Version Number": "Save the confirmed specification with a version number."
            },
            "Version Control": {
                "Save to Database": "Save the specification to the database.",
                "Track Changes": "Implement version control to track changes.",
                "Revert to Previous Versions": "Allow reverting to previous versions."
            }
        }
    }
}

dict_to_opml(body, mind_map)

opml_output_path = "API_Mockup_Tool_Mind_Map.opml"
tree = ElementTree(root)
tree.write(opml_output_path, encoding="utf-8", xml_declaration=True)

opml_output_path
