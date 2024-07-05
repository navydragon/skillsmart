-- Задания
--
-- 1. Найдите все отряды, у которых нет лидера.
--
SELECT
    squad_id,
    name AS squad_name
FROM
    Squads
WHERE
    leader_id IS NULL;

-- 2. Получите список всех гномов старше 150 лет, у которых профессия "Warrior".
--
SELECT
    dwarf_id,
    name AS dwarf_name,
    age,
    profession
FROM
    Dwarves
WHERE
    age > 150
    AND profession = 'Warrior';

-- 3. Найдите гномов, у которых есть хотя бы один предмет типа "weapon".
--
SELECT DISTINCT
    D.dwarf_id,
    D.name AS dwarf_name,
    D.age,
    D.profession
FROM
    Dwarves D
INNER JOIN
    Items I ON D.dwarf_id = I.owner_id
WHERE
    I.type = 'weapon';

-- 4. Получите количество задач для каждого гнома, сгруппировав их по статусу.
--
SELECT
    T.assigned_to AS dwarf_id,
    D.name AS dwarf_name,
    T.status,
    COUNT(T.task_id) AS task_count
FROM
    Tasks T
INNER JOIN
    Dwarves D ON T.assigned_to = D.dwarf_id
GROUP BY
    T.assigned_to,
    D.name,
    T.status;

-- 5. Найдите все задачи, которые были назначены гномам из отряда с именем "Guardians".
--
SELECT
    T.task_id,
    T.description,
    T.assigned_to AS dwarf_id,
    D.name AS dwarf_name,
    S.squad_id,
    S.name AS squad_name
FROM
    Tasks T
INNER JOIN
    Dwarves D ON T.assigned_to = D.dwarf_id
INNER JOIN
    Squads S ON D.squad_id = S.squad_id
WHERE
    S.name = 'Guardians';

-- 6. Выведите всех гномов и их ближайших родственников, указав тип родственных отношений.
SELECT
    D1.dwarf_id AS dwarf_id,
    D1.name AS dwarf_name,
    D2.dwarf_id AS relative_id,
    D2.name AS relative_name,
    R.relationship
FROM
    Relationships R
JOIN
    Dwarves D1 ON R.dwarf_id = D1.dwarf_id
JOIN
    Dwarves D2 ON R.related_to = D2.dwarf_id;
