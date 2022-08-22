# Data Manipulation (SQL, R, Python)

This page shows how to manipulate data in SQL, R & Python.

**Contents:**

- Selecting Columns
- Filtering Rows
- Aggregate Functions
- Sorting and Grouping
- Getting data across multiple tables using JOIN

## Setup

- SQL: there is nothing to setup, this is based on PostgreSQL
- R: We will use the "dplyr" package for data manipulation
- Python: We will use the "pandas" package for manipulation

# SQL

## Selecting Columns

A query is a request for data from database table (or combination of tables).

In SQL you can select data from a table using a SELECT statement. For example, the following query selects the variable1 column from the table1 table (it is good practice to make SQL keywords uppercase to distinguish them from other parts of your query, like column and table variables):

SQL:

```sql
-- SQL
-- Comments look like this!
SELECT variable1
FROM table1;

-- Select multiple columns
SELECT variable1, variable2
FROM table1;

-- Select all columns
SELECT *
FROM table1;

-- Only view selected number of results
SELECT *
FROM table1
LIMIT 10;

-- Get unique values
SELECT DISTINCT variable3
FROM table2;

-- Counts all rows in table
SELECT COUNT(*)
FROM table1;

-- Count all rows in column (non-missing)
SELECT COUNT(variable2)
FROM table1;

-- Count distinct variable2s
SELECT COUNT(DISTINCT variable2)
FROM table1;

-- If you want to save your results into a table, use INTO
SELECT variable1, variable2
INTO newTable
FROM table1;

```

## Filtering rows

We can filter based on the WHERE keyword with any of the comparison operators:

- `= equal`
- `<> not equal`
- `< less than`
- `> greater than`
- `< = less than or equal to`
- `> = greater than or equal to`

In action:

```sql
-- Get all data from table2 where variable 4 is term
SELECT variable4
FROM table2
WHERE variable4 = 'term';

-- Example 2
SELECT *
FROM table2
WHERE variable5 = 2016;

SELECT *
FROM table2
WHERE variable3 = 'otherterm';

```

***WHERE ALWAYS COMES AFTER FROM***

The AND clause can be used for multiple conditions:

```sql
SELECT variable4
FROM table2
WHERE variable5 > 1994
AND variable5 < 2000;

```

**You need to specify the column variable1 separately for every AND condition.**

The OR works where some but not all of the conditions need to be met:

```sql
SELECT variable4
FROM table2
WHERE variable5 = 1994
OR variable5 = 2000;

-- Including both
SELECT variable4
FROM table2
WHERE (variable5 = 1994 OR variable5 = 1995)
AND (variable6 = 'PG' OR variable6 = 'R');

```

To get items in between values you can use the BETWEEN clause:

```sql
-- BETWEEN is inclusive so 1994 and 2000 will be included in results
SELECT variable4
FROM table2
WHERE variable5
BETWEEN 1994 AND 2000;

-- Example 2
SELECT variable1
FROM table3
WHERE variable7 BETWEEN 2 AND 12
AND variable6 = 'USA';

-- Example 3
SELECT variable4, variable5
FROM table2
WHERE variable5
BETWEEN 1990 AND 2000;

```

The IN operator to include specific items:

```sql
SELECT variable1
FROM table3
WHERE variable7 IN (2,4,6,8,10);

```

Missing values can be identified using NULL or ISNULL:

```sql
SELECT COUNT(*)
FROM table1
WHERE variable2 IS NULL;

-- Get non missing results
SELECT variable1
FROM table1
WHERE variable2 IS NOT NULL;

```

Searching for patterns using LIKE and NOT LIKE. We can add a wildcard to act as a placeholder for other values. The first is % which will match zero, one or my characters in text.

```sql
SELECT variable1
FROM table4
WHERE variable1 LIKE 'Patte%';

```

Will return ‘Data’ , ‘DataCamp’, ‘DataMind’.

The next wildcard is _ . This will match a single character.

```sql
SELECT variable1
FROM table4
WHERE variable1 LIKE 'P_ttern';

-- Get variable1s that don't start with P
SELECT variable1
FROM table1
WHERE variable1 NOT LIKE 'P%';

```

## Aggregate functions

Aggregate functions such as MIN, MAX, AVG, SUM

```sql
SELECT MIN(variable6)
FROM table2

```

Combine aggregate functions with WHERE

```sql
SELECT SUM(variable7)
FROM table2
WHERE variable5 >= 2010;

```

You can perform basic arithmetic too

```sql
SELECT (4 * 3);
-- Returns 12

SELECT(4 / 3);
-- Returns 1

SELECT(4.0 / 3.0) AS result;
-- Returns 1.333

```

Aliasing allows you to variable1 results when returning multiple of the same aggregated results

```sql
-- This will return 2 max columns
SELECT MAX(variable7), MAX(variable6)
FROM table2;

-- will return clearer results
SELECT MAX(variable7) AS max_variable7, MAX(variable6) AS max_variable6
FROM table2;

```

## Sorting and grouping

We can sort data using ORDER BY.

It defaults to ascending so if you want to go descending you need to specify.

```sql
-- ascending
SELECT variable1
FROM table1
ORDER BY variable1;

-- descending
SELECT variable1
FROM table1
ORDER BY variable1 DESC;

-- order by two columns
SELECT variable1, variable2
FROM table1
ORDER BY variable1, variable2;

```

You can aggregate results using GROUP BY.

```sql
SELECT variable8, COUNT(*)
FROM table5
GROUP BY variable8;

```

We can also order our results

```sql
SELECT variable5, variable8
FROM table2
GROUP BY variable5, variable8
ORDER BY variable5, variable8;

```

In SQL, aggregate functions can't be used in WHERE clauses. This means that if you want to filter based on the result of an aggregate function, you need another way! That's where the HAVING clause comes in. For example:

```sql
SELECT variable5
FROM table2
GROUP BY variable5
HAVING COUNT(variable4) > 10;

```

Putting it all together

```sql
SELECT variable5, AVG(variable7) AS avg_variable7, AVG(variable9) AS avg_variable9
FROM table2
WHERE variable5 > 1990
GROUP BY variable5
HAVING AVG(variable7) > 60000000
ORDER BY avg_variable9 DESC;

```

## Getting data across multiple tables using JOIN

In the real world however, you will often want to query multiple tables.

In this case, you'd want to get the ID of all of the people from `table_ids` and then use it to get their `name` from `table_names` . In SQL, this concept is known as a **join**, and a basic join is shown in the editor to the right.

The query in the editor gets the IMDB score for the film *To Kill a Mockingbird*! Cool right?

```sql
-- Select the variables you are interested in
SELECT id, name
-- We are getting id's from table_ids
FROM table_ids
-- We are getting the names of those with the id from table_names
JOIN table_names
-- We are joining the two tables by ID and name
ON table_ids.id = table_names.name
-- And we are selecting only those with the specified id
WHERE id = '1234';
```

# R

```r
# R

# Import library for manipulation
library("dplyr") # dplyr enables the "%>%" filter tool

# Comments look like this!
table1 %>% select(variable1)

# Select multiple columns
table1 %>% select(variable1, variable2)

# Select all columns
table1

# Only view selected number of results
head(table1)

# Get unique values
unique(table1$variable3)

# Counts all rows in table
nrow(table1)

# Count all rows in column (non-missing)
nrow(table1)

# Count distinct variable2s
length(unique(table1$variable2))

# If you want to save your results into a table, assign it to a table
newTable <- table1 %>% select(variable1, variable2)

```

# Python

```python
# Python

# Import library for manipulation
Import pandas as pd

# Comments look like this!
table1 = table1[[variable1]]

# Select multiple columns
table1 = table1[[variable1, variable2]]

# Select all columns
table1

# Only view selected number of results
table1.head()

# Get unique values
table1[variable1].unique()

# Counts all rows in table
table1.shape

# Count all rows in column (non-missing)
#??

# Count distinct variable2s
len(table1[variable1].unique())

# If you want to save your results into a table, assign it to a table
newTable = table1[[variable1, variable2]]
```

---

Return to the [HOME PAGE](../HOME%20PAGE%20cafb76a874194fb8b0f554098f2830eb.md).