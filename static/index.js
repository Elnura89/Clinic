
function func(){
        var specialityId = document.getElementById('id_speciality').value;
        
        // Выполнение запроса с использованием fetch
        fetch('/api/get_doctors/' + specialityId + '/')
            .then(response => response.json())
            .then(data => {

                var doctorsContainer = document.getElementById('doctors_con');

                // Получаем все дочерние элементы
                var children = doctorsContainer.children;

                // Проходим по всем дочерним элементам и удаляем те, у которых id не равен 'doctors'
                for (var i = children.length - 1; i >= 0; i--) {
                    var child = children[i];
                    if (child.id !== 'doctors') {
                        doctorsContainer.removeChild(child);
                    }
                }

                // Очистка текущих опций второго select
                var doctorSelect = document.getElementById('doctors');
                doctorSelect.innerHTML = '';
                doctorSelect.style.display = 'block';
                console.log(doctorSelect);

                for(let i = 0;i<data.length;i++){
                    var option = document.createElement('option');
                    option.value = data[i].id;
                    option.text = data[i].name;
                    doctorSelect.appendChild(option);
                }

                
            })
            .catch(error => console.error('Error:', error));
}
