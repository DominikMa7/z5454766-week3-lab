from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/groups', methods=['GET'])
def get_groups():
    return jsonify(groups)
   #"""
    #Route to get all groups
    #return: Array of group objects
    #"""
    # TODO: (sample response below)
    #return jsonify([
    #    {
    #        "id": 1,
    #        "groupName": "Group 1",
    #        "members": [1, 2, 3],
    #    },
    #   {
    #        "id": 2,
    #        "groupName": "Group 2",
    #        "members": [4, 5],
    #    },
    #])

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)
    # """
    # Route to get all students
    # return: Array of student objects
    # """
    # TODO: (sample response below)
    # return jsonify([
    #     {"id": 1, "name": "Alice"},
    #     {"id": 2, "name": "Bob"},
    #     {"id": 3, "name": "Charlie"},
    #     {"id": 4, "name": "David"},
    #     {"id": 5, "name": "Eve"},
    # ])

@app.route('/api/groups', methods=['POST'])
def create_group():
    """
    Route to add a new group
    param groupName: The name of the group (from request body)
    param members: Array of member names (from request body)
    return: The created group object
    """
    
    # Getting the request body (DO NOT MODIFY)
    group_data = request.json
    group_name = group_data.get("groupName")
    group_members = group_data.get("members")

    invalid_members = [member_id for member_id in group_members if not get_student_by_id(member_id)]
    if valid_members:
        abort(400, description=f"Invalid member IDs: {invalid_members}")
    
    # TODO: implement storage of a new group and return their info (sample response below)
    new_id = max([group["id"] for group in groups], default=0) + 1
    new_group = {
        "id": new_id,
        "groupName": group_name,
        "members": group_members
    }
    groups.append(new_group)
    return jsonify(new_group), 201
    # return jsonify({
    #     # "id": 3,
    #     # "groupName": "New Group",
    #     # "members": [1, 2],
    # }), 201

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    global get_groups
    for group in groups:
        if group["id"] == group_id:
            groups = [g for g in groups if g["id"] != group_id]
    # """
    # Route to delete a group by ID
    # param group_id: The ID of the group to delete
    # return: Empty response with status code 204
    # """
    # TODO: (delete the group with the specified id)

    return '', 204  # Return 204 (do not modify this line)
    abort(404, description="Group not found")

@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    for group in groups:
        if group["id"] == group_id:
            member_details = []
            for member_id in group ["members"]:
                student = get_student_by_id(member_id)
                if student:
                    member_details.append(student)
            return jsonify({
                "id": group["id"],
                "groupName": group["groupName"],
                "members": member_details
            })
    abort(404, description="Group not found")
    # """
    # Route to get a group by ID (for fetching group members)
    # param group_id: The ID of the group to retrieve
    # return: The group object with member details
    # """
    # # TODO: (sample response below)
    # return jsonify({
    #     "id": 1,
    #     "groupName": "Group 1",
    #     "members": [
    #         {"id": 1, "name": "Alice"},
    #         {"id": 2, "name": "Bob"},
    #         {"id": 3, "name": "Charlie"},
    #     ],
    # })
    # # TODO:
    # # if group id isn't valid:
    # #     abort(404, "Group not found")

if __name__ == '__main__':
    app.run(port=3902, debug=True)

