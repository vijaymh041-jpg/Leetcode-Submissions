-- Last updated: 6/12/2026, 12:45:04 AM
# Write your MySQL query statement below
select person.firstName, person.lastName, Address.city, Address.state from person left join Address on Person.personID = Address.PersonID order by firstName;