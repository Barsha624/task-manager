const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

async function loadTasks() {
    const response = await fetch("/tasks");
    const data = await response.json();

    console.log(taskList);
    console.log(data.tasks.length);

    console.log(data);

    taskList.innerHTML = "";

    if (data.tasks.length === 0) {
        taskList.innerHTML = "<p>No tasks yet. Add your first task!</p>";
        return;
    }

    data.tasks.forEach(task => {
        const taskItem = document.createElement("div");
        taskItem.className = "task-item";

        const taskName = document.createElement("span");
        taskName.textContent = task.title;

        if (task.completed === 1) {
            taskName.classList.add("completed");
        }

        taskItem.appendChild(taskName);
        taskList.appendChild(taskItem);
    });
}

async function addTask() {
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task!");
        return;
    }

    const response = await fetch("/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: taskText
        })
    });

    if (response.ok) {
        taskInput.value = "";
        loadTasks();
    }
}

addTaskBtn.addEventListener("click", addTask);

loadTasks();