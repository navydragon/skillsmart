-- 1. Получить информацию о всех гномах, которые входят в какой-либо отряд, вместе с информацией об их отрядах.
--
SELECT
    D.dwarf_id,
    D.name AS dwarf_name,
    D.age,
    D.profession,
    S.squad_id,
    S.name AS squad_name,
    S.mission
FROM
    Dwarves D
JOIN
    Squads S ON D.squad_id = S.squad_id
WHERE
    D.squad_id IS NOT NULL;

-- 2. Найти всех гномов с профессией "miner", которые не состоят ни в одном отряде.
--
SELECT
    dwarf_id,
    name,
    age,
    profession
FROM
    Dwarves
WHERE
    profession = 'miner'
    AND squad_id IS NULL;


-- 3. Получить все задачи с наивысшим приоритетом, которые находятся в статусе "pending".
--
SELECT
    task_id,
    description,
    priority,
    assigned_to,
    status
FROM
    Tasks
WHERE
    status = 'pending'
    AND priority = (SELECT MAX(priority) FROM Tasks WHERE status = 'pending');

-- 4. Для каждого гнома, который владеет хотя бы одним предметом, получить количество предметов, которыми он владеет.
--
SELECT
    owner_id AS dwarf_id,
    COUNT(item_id) AS item_count
FROM
    Items
WHERE
    owner_id IS NOT NULL
GROUP BY
    owner_id;

-- 5. Получить список всех отрядов и количество гномов в каждом отряде. Также включите в выдачу отряды без гномов.
--
SELECT
    S.squad_id,
    S.name AS squad_name,
    COUNT(D.dwarf_id) AS dwarf_count
FROM
    Squads S
LEFT JOIN
    Dwarves D ON S.squad_id = D.squad_id
GROUP BY
    S.squad_id,
    S.name;

-- 6. Получить список профессий с наибольшим количеством незавершённых задач ("pending" и "in_progress") у гномов этих профессий.
--
SELECT
    D.profession,
    COUNT(T.task_id) AS unfinished_task_count
FROM
    Dwarves D
INNER JOIN
    Tasks T ON D.dwarf_id = T.assigned_to
WHERE
    T.status IN ('pending', 'in_progress')
GROUP BY
    D.profession
ORDER BY
    unfinished_task_count DESC;


-- 7. Для каждого типа предметов узнать средний возраст гномов, владеющих этими предметами.
--
SELECT
    I.type,
    AVG(D.age)
FROM
    Items I
INNER JOIN
    Dwarves D ON I.owner_id = D.dwarf_id
GROUP BY
    I.type;

-- 8. Найти всех гномов старше среднего возраста (по всем гномам в базе), которые не владеют никакими предметами.
SELECT
    D.id,
    D.name as dwarf_name,
    D.age
FROM
    Dwarves D
LEFT JOIN
    Items I ON D.dwarf_id = I.owner_id
WHERE
    D.age > (SELECT AVG(D2.age) FROM Dwarves D2)
    AND I.item_id IS NULL;