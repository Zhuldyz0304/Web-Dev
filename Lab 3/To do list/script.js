window.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.querySelector('.write');
    const addBtn = document.querySelector('.add');
    console.log(addBtn);
    
    addBtn.addEventListener('click', function() {
        const value = taskInput.value;
        if(value) {
            generateTask(value);
            taskInput.value = '';
        }
        
    });
});

function generateTask(taskName) {
    const taskWrapper = document.querySelector('.tasks');
    const task = document.createElement('div');
    task.classList.add('new-task');

    const checkbox = document.createElement('input');
    checkbox.setAttribute('type', 'checkbox');
    task.appendChild(checkbox);
    checkbox.classList.add('done');

    const txt = document.createElement('span');
    txt.innerText = taskName;
    task.appendChild(txt);
    txt.classList.add('task-name');

    const button = document.createElement('button');
    button.setAttribute('type', 'button');
    button.classList.add('delete');

    const img = document.createElement('img');
    img.setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYI_27-lSo8Z4auY7awG1LHELDPeyiANbDnY59FbLY-K2U4jDe0C45zUp63EPDzH1buKc&usqp=CAU');
    button.appendChild(img);

    task.appendChild(button);

    taskWrapper.appendChild(task);
}
function deleteTask(task){
    removeEventListener(task)
}
