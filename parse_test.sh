#!/bin/sh

for n in 0 1 2 3 4
do
	for mode in 0 r
	do
		for input_type in h v
		do
			for parse in parsers default1 default2
			do
				for num in 0 1 2 3 4 5 6
				do
					julia ./src/parseInt_${parse}_$input_type.jl < ./test/test$input_type$mode$num.txt >> ./output/output1.txt
					echo $n $mode $input_type $parse $num "done"
				done
			done
		done
	done
done

for n in 0 1 2 3 4
do
	./src/julia using_parsers.jl >> ./output/output2.txt
done
