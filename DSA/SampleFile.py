import inspect
import os

def get_query_tag():
    frame = None
    caller = None

    try:
        frame = inspect.currentframe()
        if frame is None or frame.f_back is None:
            return {"error": "Unable to inspect caller frame"}

        caller = frame.f_back

        method_name = caller.f_code.co_name
        file_name = os.path.basename(caller.f_code.co_filename)

        locals_dict = caller.f_locals

        class_name = None
        arguments = {}

        # Case 1: method inside a class
        if "self" in locals_dict:
            obj = locals_dict["self"]
            class_name = obj.__class__.__name__
            arguments = obj.__dict__

        # Case 2: normal function
        else:
            arguments = locals_dict

        dim_abr = arguments.get("dim_abr", "NA")
        cycle_date = arguments.get("cycle_date", "NA")

        tag_id = f"{dim_abr}_{cycle_date}_{class_name or method_name}"

        return {
            "file_name": file_name,
            "class_name": class_name,
            "method_name": method_name,
            "tag_id": tag_id
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        del frame
        del caller
