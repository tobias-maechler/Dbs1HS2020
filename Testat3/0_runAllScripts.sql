-- Autoren: Kevin Löffler & Tobias Mächler
-- psql -U postgres -v ON_ERROR_STOP=on -f 0_runAllScripts.sql
\echo \conninfo
\echo
\echo -n 'client encoding: '\encoding
\echo

SET client_min_messages = ERROR;
\set user pokeruser
\set password '\'poker\''
\set database poker
\set promptvar ''

\prompt 'DROP USER [':user'] and DROP DATABASE [':database'] if existing (\\q or Ctrl-C to abort)?' promptvar
:promptvar

DROP DATABASE if exists :database;
DROP USER if exists :user;

\echo -------------------------------------
\echo passwort for user :user = :password
\echo -------------------------------------
\echo

\prompt 'CREATE USER [':user'] and DATABASE [':database'] (\\q or Ctrl-C to abort)?' promptvar
:promptvar

CREATE USER :user WITH PASSWORD :password;
CREATE DATABASE :database WITH OWNER :user ENCODING 'UTF8';
\echo
\c :database :user

-- specify encoding to match your files encoding, usually UTF8
-- valid values are: 'UTF8', 'LATIN1', 'WIN1252'
\encoding 'UTF8'

-- create extensions
--\ir 1_extensions.sql

-- create schema
\echo
\echo 'run 2_schema.sql'
\ir 2_schema.sql

-- insert data in slo-mo or use COPY for speedup
--\ir 3_inserts.sql
\echo
\echo 'run 3_inserts.sql'
\ir 3_inserts.sql

-- create primary keys, constraints, indexes
\echo
\echo 'run 4_constraints.sql'
\ir 4_constraints.sql

\echo
\prompt 'Execute Queries (\\q or Ctrl-C to abort)?' promptvar
:promptvar

-- set client encoding for query results to auto
-- > adjust if the detected default is not what you want
-- valid values are: 'UTF8', 'LATIN1', 'WIN1252'
\encoding 'auto'

\set ECHO queries
-- query the database
\ir 5_queries.sql

\echo 'End of script. View the source code including the webscraper and python script at https://github.com/tobias-maechler/Dbs1HS2020'
