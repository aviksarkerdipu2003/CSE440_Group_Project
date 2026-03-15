# CSE440_Group_Project
Group no : 4  
**Project Task:** Create a puzzle-solver that efficiently tackles diverse puzzles using multiple search algorithms, with customized heuristics for informed searches. It offers user-friendly input, algorithm selection, and performance comparison, with thorough documentation for analysis.

**Collaborators:**
 |**Name**|**Student ID**|
 |-----|---------|
 |Sazzad Hosen Sany| 2211380042|
 |Avik Sarker Dipu| 2111532042|
 |Argho Das| 2131313042|
 |Md Samiullah Shekh| 2011417042|


## Project Structure:

```
puzzle_solver/
│
├── app/
│   ├── streamlit_app.py
│   ├── pages/
│   │   ├── 1_Puzzle_Solver.py
│   │   ├── 2_Algorithm_Comparison.py
│   │   └── 3_Documentation.py
│
├── core/
│   ├── problem.py
│   ├── state.py
│   ├── node.py
│   ├── metrics.py
│   └── utils.py
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dls.py
│   ├── iddfs.py
│   ├── ucs.py
│   ├── greedy.py
│   ├── astar.py
│   └── beam.py
│
├── puzzles/
│   ├── 8_puzzle/
│   │   ├── puzzle.py
│   │   ├── heuristics.py
│   │   ├── parser.py
│   │   └── samples.py
│   │
│   ├── maze/
│   │   ├── puzzle.py
│   │   ├── heuristics.py
│   │   ├── parser.py
│   │   └── samples.py
│   │
│   └── sudoku/
│       ├── puzzle.py
│       ├── heuristics.py
│       ├── parser.py
│       └── samples.py
│
├── benchmarks/
│   ├── runner.py
│   ├── datasets.py
│   └── charts.py
│
├── tests/
│   ├── test_algorithms.py
│   ├── test_8puzzle.py
│   ├── test_maze.py
│   └── test_sudoku.py
│
├── docs/
│   ├── proposal.md
│   ├── architecture.md
│   ├── algorithm_analysis.md
│   ├── user_manual.md
│   └── report_assets/
│
├── data/
│   ├── eight_puzzle_cases.json
│   ├── maze_cases.json
│   └── sudoku_cases.json
│
├── requirements.txt
├── README.md
└── run.sh
```
