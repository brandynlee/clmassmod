#!/bin/bash

for snap in 41 54; do

    for sampling in 0 3 4; do

	for noise in 0 1 2 3; do

	    for r in 8 9 10; do

		for mc in zhaomc c4 cfree; do

		    for prior in log linear; do

			config=${prior}-${mc}-r${r}-n${sampling}_${noise}
			dir=../mxxl_imperial/snap$snap/$config
			mkdir $dir
			cat base.sh mxxl.sh ${prior}prior.sh ${mc}.sh r${r}.sh n${sampling}_${noise}.sh > $dir/config.sh

			echo $config >> ../run6

		    done

		done

	    done

	done

    done

done
	