from tabulate import tabulate

class ProjectPlan:

    page = "Project Plan/n/n/n"

    user_input = {
        # Dicts are ordered as of python 3.6
        "Links": "Yes",
        "KeyPersonnel": "Yes",
        "ProjectPlan": "Yes",
        "MeetingNotes": "Yes",
        "NextSteps": "Yes",
        "ExecutiveView": "Yes"
        # Note: Need a class for users -- should check for libraries
    }


    def add(self, section_name):
        self.page = self.page + section_name

    def add_table(self, table):
        self.page = self.page + table

    def __init__(self, user_input):
        print("Self built for ProjectPlan")
        self.user_input = user_input

        # fix the below - it says it doesn't have enough values to unpack - removed , input
        for inputKey in user_input:
            print("InputKey is " + str(inputKey) + " and input is ")
            if input == "Yes":
                print("Input Yes, adding table to page")
                #add("/n/n/n" + InputKey)
                #add_table(Table(inputKey))

            else:
                print("Input was No, excluding section")

        print("Printing page " + page)



    class Table:
        def __init__(self, table_type):
            type = table_type
            table_data = NULL

            if type == "Links":
                table_data = [
                    ["Jira Epic", "Link TBD"],
                    ["Jira Dashboard (if applicable)", "Link TBD"],
                    ["LucidChart Diagram (if applicable)", "Link TBD"],
                    ["Confluence", "Link TBD"]
                ]

                header = ""

            elif type == "KeyPersonnel":
                table_data = [
                    ["", "TBD"],
                    ["", "TBD"],
                    ["", "TBD"],
                ]

                header = {"Project Role", "Name", "Comment"}

            elif type == "ProjectPlan":
                print("Project plan")

            table = tabluate(table_data, headers=header, tablefmt="grid")
            print("Table created")


#                "MeetingNotes": "Yes",
#                "NextSteps": "Yes",
#                "ExecutiveView": "Yes"




