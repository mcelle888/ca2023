drop table students cascade;
drop table teachers cascade;
drop table subjects cascade;
drop table enrollments cascade;

-- Students

create table students (
    student_id serial primary key,

    f_name text not null,
    l_name text not null,
    dob date
);

-- Teachers

create table teachers (
    teacher_id serial primary key,

    name text not null

);
-- Subjects

create table subjects (
    subject_id serial primary key,

    subject_name text not null,
    teacher_id integer,

    foreign key (teacher_id) references teachers (teacher_id) on delete set null
);

-- Enrollments

create table enrollments (
    enrollments_id serial primary key,
    enrollment_date date default current_date,
    student_id integer not null,
    subject_id integer not null,

    foreign key (student_id) references students (student_id) on delete cascade,
    foreign key (subject_id) references subjects (subject_id) on delete cascade
);
    
