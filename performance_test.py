from test import*
import cProfile
import pstats

if __name__ == "__main__":
	cProfile.run('run_program()', filename = "performance_result.stats")
	p=pstats.Stats('performance_result.stats')
	
	p.sort_stats('cumulative')
	p.print_stats(10)