IN="7sj-ighm-742q3w4t"

for I in $(seq 25); do
    echo $I $IN | tr $(printf %${I}s | tr ' ' '.')\A-Z A-ZA-Z
done