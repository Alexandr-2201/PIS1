var groupmates = [
    {
        "name": "Александр",
        "surname": "Попов",
	"group": "БСТ2201",
        "marks": [4, 5, 2]
    },
    {
        "name": "Наталья",
        "surname": "Прохорова",
	"group": "БСТ2201",
        "marks": [5, 4, 5]
    },
    {
        "name": "Сеня",
        "surname": "Кузин",
	"group": "БСТ2202",
        "marks": [4, 2, 1]
    },
    {
        "name": "Олег",
        "surname": "Азаров",
	"group": "БСТ2201",
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Николаев",
	"group": "БСТ2202",
        "marks": [5, 4, 3]
    },
    {
        "name": "Петр",
        "surname": "Петров",
	"group": "БСТ2203",
        "marks": [2, 3, 1]
    }
];

var rpad = function(str, length) {
	// js не поддерживает добавление нужного количества символов
	// справа от строки, т.е. аналога ljust из Python здесь нет 
	str = str.toString(); // преобразование в строку
	while (str.length < length)
		str = str + ' '; // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
	return str;
};

// Функция для вычисления среднего балла
var getAvgMark = function(student) {
	return student['marks'].reduce((a, b) => a + b, 0) / student['marks'].length;
};

var printStudents = function(students){ 
	console.log(
		rpad("Имя", 15),
		rpad("Фамилия", 15),
		rpad("Группа", 8),
		rpad("Оценки", 20),
        	rpad("Средний балл", 15)
	);
	// был выведен заголовок таблицы
	for (var i = 0; i<=students.length-1; i++){
		// в цикле выводится каждый экземпляр студента 
		console.log(
			rpad(students[i]['name'], 15),
			rpad(students[i]['surname'], 15),
			rpad(students[i]['group'], 8),
			rpad(students[i]['marks'], 20),
            		rpad(students[i]['avgMark'].toFixed(2), 15)
		);
	}
	console.log('\n'); // добавляется пустая строка в конце вывода
};

// Функция фильтрации по группе
var filterByGroup = function(students, group) {
    return students.filter(function(student) {
        return student.group === group;
    });
};

// Функция фильтрации по среднему баллу
var filterByAvgMark = function(students, minAvg) {
    return students.filter(function(student) {
        return student.avgMark > minAvg;
    });
};


// Выполнение
for (var i = 0; i < groupmates.length; i++) {
    groupmates[i].avgMark = getAvgMark(groupmates[i]);
}
printStudents(groupmates);

var targetGroup = prompt("Введите название группы для фильтрации:");
var filteredByGroup = filterByGroup(groupmates, targetGroup);
console.log("Студенты группы " + targetGroup + ":");
if (filteredByGroup.length > 0) {
    printStudents(filteredByGroup);
} else {
    console.log("Студентов в данной группе не найдено.\n");
}

// Фильтрация по среднему баллу
var minAvg = parseFloat(prompt("Введите минимальный средний балл для фильтрации:"));
var filteredByMark = filterByAvgMark(groupmates, minAvg);
console.log("Студенты со средним баллом выше " + minAvg + ":");
if (filteredByMark.length > 0) {
    printStudents(filteredByMark);
} else {
    console.log("Студентов с таким средним баллом не найдено.\n");
}