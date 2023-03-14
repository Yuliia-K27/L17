-- Запит для перерахування кількості вакансій у таблиці employee
SELECT COUNT(*) AS vacancy_count
FROM employee
WHERE hire_date IS NULL;

-- Запит для отримання середньої зарплати та кількості працівників відділу 90
SELECT AVG(salary) AS avg_salary, COUNT(*) AS employee_count
FROM employee
WHERE department_id = 90;

-- Запит для отримання кількості працівників з тією самою роботою
SELECT job_title, COUNT(*) AS employee_count
FROM employee
GROUP BY job_title
HAVING COUNT(*) > 1;

-- Запит для знаходження імені (ім'я, прізвище), коду відділу та імені всіх співробітників
SELECT CONCAT(first_name, ' ', last_name) AS full_name, department_id, job_title
FROM employee;

-- Запит для знаходження імені (ім'я, прізвище), роботи, ідентифікатора відділу та імен співробітників, які працюють в Лондоні
SELECT CONCAT(first_name, ' ', last_name) AS full_name, job_title, department_id, city
FROM employee
WHERE city = 'London';
