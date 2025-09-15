with A as (
    select
        *,
        dense_rank() over (order by salary desc) as rnk
    from Employee
)

select iif(
    (select count(*) from A where rnk = 2) = 0,
    null,
    (select top(1) salary from A where rnk = 2)) as SecondHighestSalary