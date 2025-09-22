from js import document
from pyscript import Element

def generate_message(event=None):
    name = Element("name").element.value.strip()
    age = Element("age").element.value.strip()
    school = Element("school").element.value.strip()

    if not name or not age or not school:
        Element("output").write("<b style='color:red'>⚠ Please fill in all fields.</b>")
        return

    try:
        age_num = int(age)
    except ValueError:
        Element("output").write("<b style='color:red'>⚠ Age must be a number.</b>")
        return

    profile = f"""
    <b>🎓 Student Profile</b><br>
    Name  : {name}<br>
    Age   : {age_num}<br>
    School: {school}<br><br>

    <b>📝 Notes:</b><br>
    {name} is currently {age_num} years old and studies at {school}.<br>
    This information was gathered through input fields and displayed using a 
    multiline string in Python via PyScript.
    """

    Element("output").write(profile)

# connect button click to Python function
document.getElementById("generate-btn").addEventListener("click", generate_message)