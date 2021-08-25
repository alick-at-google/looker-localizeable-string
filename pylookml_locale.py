import looker_sdk
import lookml
import csv

repos = [
    ["looker/democorp_thelookevent", "thelook_event"],
    ["looker/saas_demo", "sfdc_demo"],
    ["looker/new_demo_adwords", "digital_marketing"],
    ["looker/retail_demo", "retail"],
    ["looker/healthcare_demo", "healthcare"],
    ["looker/financial_services_demo", "retail_banking"],
    ["looker/call_center_demo", "call_center"],
    ["llooker/student_success", "student_success"]]


with open('locale.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for repo in repos:
        proj = lookml.Project(
            repo=repo[0],
            # Optional args for the deploy URL (for deploying directly to prodcution mode)
            access_token={access_token_goes_here}, looker_host="https://googledemo.looker.com/", looker_project_name=repo[1], index_whole=True
        )

        # go through files in github
        for file in proj.files():
            print(file.name)
            # go through views
            if(file.name != "user_order_facts_refinements.view.lkml"):
                for v in file.views:
                    print(v.name)

                    # print(v)
                    # go through each field
                    for field in v.fields():
                        for param in ("label", "group_label", "group_item_label", "description", "view_label"):
                            if param in field:
                                spamwriter.writerow([proj._repo, file.path, v.name, type(
                                    field), field.name, param,  field[param].value])

                        # go through action param
                        if "action" in field:
                            for action in field.action:
                                spamwriter.writerow([proj._repo, file.path, v.name, type(
                                    field), field.name, "action label",  action.label.value])
                                # find action form param labels
                                if "form_params" in action:
                                    for form_param in action.form_params:
                                        # test next 2 lines
                                        if form_param.label is not None:
                                            spamwriter.writerow([proj._repo, file.path, v.name, type(
                                                field), field.name, "form_param label",  form_param.label.value])
                                        if form_param.description is not None:
                                            spamwriter.writerow([proj._repo, file.path, v.name, type(
                                                field), field.name, "form_param description",  form_param.description.value])
                                        if "options" in form_param:
                                            for option in form_param.options:
                                                spamwriter.writerow([proj._repo, file.path, v.name, type(
                                                    field), field.name, "option label",  option.label.value])
