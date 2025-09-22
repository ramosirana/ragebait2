from js import document
from pyscript import Element

score = float(element("score1").element.value)
score1 = float(element("score2").element.value)
def avg(score1 + score2 / 2)
def compute_average(event=None):
    try:
        Element("average").write(f"Average: {avg:.1f}")
        Element("result").write(f"Passed? {'Yes' if avg >= 75 else 'No'}")

    except ValueError:
        Element("average").write("Average: Invalid input")
        Element("result").write("Passed? -")

document.getElementById("compute-btn").addEventListener("click", compute_average)