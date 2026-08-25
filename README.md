# Background

SQL sublanguage: DML (Data Manipulation Language)

To update a record we utilize the UPDATE keyword.

UPDATE table_name SET col_1 = val_1, col_2 = val_2, ...col_N = val_N WHERE condition;

NOTE: The WHERE condition is important - leaving it out will update that column throughout all records in the
table.

## Problem 1

Assume the following table already exists.

| id | firstname | lastname |
|----|-----------|----------|
| 1 | Steve | Garcia |
| 2 | Alexa | Smith |
| 3 | Steve | Jones |
| 4 | Brandon | Smith |
| 5 | Adam | Jones |

Write a statement in `problem1.sql` to update Alexa's last name to 'Rush' in the `site_user` table.
