if [ "$#" -ne 2 ]; then
    echo "Input l and r ."
    exit 1
fi
l=$1
r=$2

echo "Expect: $(echo $l $r | python Eg.py)"
echo "Actual: $(echo $l $r | python E.py)"
