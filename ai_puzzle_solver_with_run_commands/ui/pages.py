import pandas as pd
import streamlit as st

from data.samples import EIGHT, MAZES, SUDOKUS
from puzzles.eight_puzzle import EightPuzzleProblem, ep_manhattan, parse_8
from puzzles.maze import MazeProblem, maze_manhattan, parse_maze
from puzzles.sudoku import SudokuProblem, sudoku_h, parse_sudoku
from algorithms.search import bfs, dfs, dls, iddfs, ucs, greedy, astar, beam

def problem_builder(ptype,mode,payload):
    if ptype=="8 Puzzle":
        return EightPuzzleProblem(EIGHT[payload] if mode=="Sample" else parse_8(payload))
    if ptype=="Maze":
        if mode=="Sample":
            s=MAZES[payload]; return MazeProblem(s["grid"],s["start"],s["goal"])
        return MazeProblem(parse_maze(payload["grid"]), tuple(map(int,payload["start"].split(","))), tuple(map(int,payload["goal"].split(","))))
    return SudokuProblem(SUDOKUS[payload] if mode=="Sample" else parse_sudoku(payload))

def run(problem,ptype,algo,dlim=20,ilim=30,bw=2):
    if algo=="BFS": return bfs(problem)
    if algo=="DFS": return dfs(problem)
    if algo=="DLS": return dls(problem,dlim)
    if algo=="IDDFS": return iddfs(problem,ilim)
    if algo=="UCS": return ucs(problem)
    h = (lambda s: ep_manhattan(s,problem.goal)) if ptype=="8 Puzzle" else ((lambda s: maze_manhattan(s,problem.goal)) if ptype=="Maze" else sudoku_h)
    if algo=="Greedy": return greedy(problem,h)
    if algo=="A*": return astar(problem,h)
    return beam(problem,h,bw)

def render_state(problem,ptype,s):
    if ptype=="8 Puzzle":
        return "\n".join(" ".join(str(x) if x!=0 else "_" for x in s[i:i+3]) for i in range(0,9,3))
    if ptype=="Maze":
        lines=[]
        for r in range(problem.rows):
            row=[]
            for c in range(problem.cols):
                row.append("A" if (r,c)==s else "S" if (r,c)==problem.start else "G" if (r,c)==problem.goal else "#" if problem.grid[r][c]==1 else ".")
            lines.append(" ".join(row))
        return "\n".join(lines)
    lines=[]
    for i,row in enumerate(s):
        if i>0 and i%3==0: lines.append("-"*21)
        parts=[]
        for j,v in enumerate(row):
            if j>0 and j%3==0: parts.append("|")
            parts.append(str(v) if v else ".")
        lines.append(" ".join(parts))
    return "\n".join(lines)

def metric_box(label,value):
    st.markdown(f"<div class='metric-card'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div></div>", unsafe_allow_html=True)

def home():
    st.markdown("""
    <div class="hero">
    <h1>🧠 AI Puzzle Solver</h1>
    <p>Create a puzzle-solver that efficiently tackles diverse puzzles using multiple search algorithms, with customized heuristics for informed searches. It offers user-friendly input, algorithm selection, and performance comparison, with thorough documentation for analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3=st.columns(3,gap="large")
    with c1:
        st.markdown("<div class='card'><div class='section-title'>🎮 Puzzle Solver</div><div class='tiny'>Solve 8 Puzzle, Maze, and Sudoku using AI search algorithms.</div></div>", unsafe_allow_html=True)
        if st.button("Open Puzzle Solver"): st.session_state.page="Puzzle Solver"; st.rerun()
    with c2:
        st.markdown("<div class='card'><div class='section-title'>📊 Algorithm Check</div><div class='tiny'>Compare algorithms by runtime, depth, solution steps, and expanded nodes.</div></div>", unsafe_allow_html=True)
        if st.button("Open Algorithm Check"): st.session_state.page="Algorithm Check"; st.rerun()
    with c3:
        st.markdown("<div class='card'><div class='section-title'>📘 Documentation</div><div class='tiny'>Understand algorithms, heuristics, inputs, and project analysis.</div></div>", unsafe_allow_html=True)
        if st.button("Open Documentation"): st.session_state.page="Documentation"; st.rerun()

def puzzle_solver():
    a,b=st.columns([6,1.4])
    with a: st.markdown("<div class='section-title'>🎮 Puzzle Solver</div>", unsafe_allow_html=True)
    with b:
        if st.button("⬅ Home"): st.session_state.page="Home"; st.rerun()

    left,right=st.columns([1.05,1.45],gap="large")
    with left:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        ptype=st.selectbox("Puzzle Type",["8 Puzzle","Maze","Sudoku"])
        algo=st.selectbox("Algorithm",["BFS","DFS","DLS","IDDFS","UCS","Greedy","A*","Beam"])
        mode=st.radio("Input Mode",["Sample","Custom"],horizontal=True)
        dlim,ilim,bw=20,30,2
        if algo=="DLS": dlim=st.slider("Depth Limit",1,80,20)
        if algo=="IDDFS": ilim=st.slider("Max Depth",1,80,30)
        if algo=="Beam": bw=st.slider("Beam Width",1,10,2)

        if ptype=="8 Puzzle":
            payload=st.selectbox("Sample",list(EIGHT.keys())) if mode=="Sample" else st.text_input("Custom 8 Puzzle","1 2 3 4 5 6 7 0 8")
        elif ptype=="Maze":
            if mode=="Sample": payload=st.selectbox("Sample",list(MAZES.keys()))
            else:
                grid=st.text_area("Maze Grid","0 0 0 0\n1 1 0 1\n0 0 0 0\n0 1 1 0",height=150)
                start=st.text_input("Start row,col","0,0")
                goal=st.text_input("Goal row,col","3,3")
                payload={"grid":grid,"start":start,"goal":goal}
        else:
            if mode=="Sample": payload=st.selectbox("Sample",list(SUDOKUS.keys()))
            else:
                payload=st.text_area("Sudoku Grid","5 3 0 0 7 0 0 0 0\n6 0 0 1 9 5 0 0 0\n0 9 8 0 0 0 0 6 0\n8 0 0 0 6 0 0 0 3\n4 0 0 8 0 3 0 0 1\n7 0 0 0 2 0 0 0 6\n0 6 0 0 0 0 2 8 0\n0 0 0 4 1 9 0 0 5\n0 0 0 0 8 0 0 7 9",height=220)

        solve=st.button("🚀 Solve Puzzle")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Result Console</div>", unsafe_allow_html=True)
        if solve:
            try:
                problem=problem_builder(ptype,mode,payload)
                path,metrics=run(problem,ptype,algo,dlim,ilim,bw)
                if not path: st.error("No solution found.")
                else:
                    st.success("Solution found.")
                    c1,c2,c3,c4=st.columns(4)
                    with c1: metric_box("Steps",metrics["solution_length"])
                    with c2: metric_box("Expanded",metrics["nodes_expanded"])
                    with c3: metric_box("Max Depth",metrics["max_depth"])
                    with c4: metric_box("Time",f'{metrics["elapsed_time_sec"]:.4f}s')
                    st.markdown("### Solution Path")
                    if len(path)>40: st.info(f"Showing first 40 states out of {len(path)}.")
                    for i,s in enumerate(path[:40]):
                        st.markdown(f"**Step {i}**")
                        st.code(render_state(problem,ptype,s))
            except Exception as e: st.error(f"Error: {e}")
        else: st.info("Choose puzzle, algorithm, and click Solve Puzzle.")
        st.markdown("</div>", unsafe_allow_html=True)

def algorithm_check():
    a,b=st.columns([6,1.4])
    with a: st.markdown("<div class='section-title'>📊 Algorithm Check</div>", unsafe_allow_html=True)
    with b:
        if st.button("⬅ Home",key="back2"): st.session_state.page="Home"; st.rerun()

    left,right=st.columns([1,1.5],gap="large")
    with left:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        ptype=st.selectbox("Puzzle Type",["8 Puzzle","Maze","Sudoku"],key="cmp")
        sample=st.selectbox("Sample",list(EIGHT.keys()) if ptype=="8 Puzzle" else list(MAZES.keys()) if ptype=="Maze" else list(SUDOKUS.keys()))
        algos=st.multiselect("Algorithms",["BFS","DFS","DLS","IDDFS","UCS","Greedy","A*","Beam"],default=["BFS","DFS","UCS","Greedy","A*"])
        go=st.button("Run Comparison")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        if go:
            rows=[]
            for algo in algos:
                try:
                    problem=problem_builder(ptype,"Sample",sample)
                    path,m=run(problem,ptype,algo)
                    rows.append({"Algorithm":algo,"Solved":path is not None,"Steps":len(path)-1 if path else None,"Nodes Expanded":m["nodes_expanded"],"Max Depth":m["max_depth"],"Time (sec)":round(m["elapsed_time_sec"],6)})
                except Exception as e:
                    rows.append({"Algorithm":algo,"Solved":False,"Error":str(e)})
            df=pd.DataFrame(rows)
            st.dataframe(df,use_container_width=True,hide_index=True)
            for col in ["Time (sec)","Nodes Expanded","Steps"]:
                if col in df and df[col].notnull().any():
                    st.subheader(col)
                    st.bar_chart(df[["Algorithm",col]].dropna().set_index("Algorithm"))
        else: st.info("Select algorithms and run comparison.")
        st.markdown("</div>", unsafe_allow_html=True)

def documentation():
    a,b=st.columns([6,1.4])
    with a: st.markdown("<div class='section-title'>📘 Documentation</div>", unsafe_allow_html=True)
    with b:
        if st.button("⬅ Home",key="back3"): st.session_state.page="Home"; st.rerun()

    st.markdown("""
    <div class="glass">
    <h3>Project Overview</h3>
    <p>This project creates a puzzle-solver that efficiently tackles diverse puzzles using multiple search algorithms, with customized heuristics for informed searches. It offers user-friendly input, algorithm selection, and performance comparison, with documentation for analysis.</p>

    <h3>Supported Puzzles</h3>
    <ul>
    <li><b>8 Puzzle:</b> sliding tile puzzle where 0 represents the blank tile.</li>
    <li><b>Maze:</b> grid-based pathfinding where 0 is open and 1 is blocked.</li>
    <li><b>Sudoku:</b> 9x9 constraint puzzle solved through search-based state expansion.</li>
    </ul>

    <h3>Algorithms</h3>
    <ul>
    <li><b>BFS:</b> explores level by level and gives shortest path for equal-cost problems.</li>
    <li><b>DFS:</b> explores deeply first but may not give the shortest path.</li>
    <li><b>DLS:</b> DFS with a depth limit.</li>
    <li><b>IDDFS:</b> repeatedly applies DLS with increasing depth.</li>
    <li><b>UCS:</b> expands the lowest path-cost node first.</li>
    <li><b>Greedy:</b> uses only heuristic estimate.</li>
    <li><b>A*:</b> combines path cost and heuristic for informed search.</li>
    <li><b>Beam Search:</b> keeps only the best few states at each level.</li>
    </ul>

    <h3>Heuristics</h3>
    <ul>
    <li><b>8 Puzzle:</b> Manhattan distance.</li>
    <li><b>Maze:</b> Manhattan distance from current position to goal.</li>
    <li><b>Sudoku:</b> number of empty cells remaining.</li>
    </ul>

    <h3>Performance Metrics</h3>
    <ul>
    <li>Solution steps</li>
    <li>Nodes expanded</li>
    <li>Maximum depth reached</li>
    <li>Execution time</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
