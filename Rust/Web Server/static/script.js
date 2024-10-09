function addTask(columnId) {
    const taskInput = document.getElementById("new-task");
    const taskText = taskInput.value.trim();

    if (taskText) {
        const task = document.createElement("div");
        task.className = "task";
        task.innerText = taskText;

        task.onclick = function () {
            moveTask(task, columnId);
        };

        document.getElementById(columnId).querySelector('.tasks').appendChild(task);
        taskInput.value = ""; // Clear input field
    } else {
        alert("Veuillez entrer une tâche !");
    }
}

function moveTask(task, fromColumnId) {
    const columns = ["todo", "in-progress", "done"];
    const currentIndex = columns.indexOf(fromColumnId);
    const nextIndex = (currentIndex + 1) % columns.length; // Cycle through columns

    const nextColumnId = columns[nextIndex];
    document.getElementById(nextColumnId).querySelector('.tasks').appendChild(task);
}
