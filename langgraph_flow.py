from langgraph.graph import StateGraph

from agents.parser_agent import parse_resume
from agents.evaluator_agent import evaluate_resume
from agents.ai_detector_agent import detect_ai
from agents.scoring_agent import scoring
from agents.ranking_agent import ranking
from agents.decision_agent import decision

workflow = StateGraph()

workflow.add_node("parser", parse_resume)
workflow.add_node("evaluator", evaluate_resume)
workflow.add_node("ai_detector", detect_ai)
workflow.add_node("scoring", scoring)
workflow.add_node("ranking", ranking)
workflow.add_node("decision", decision)

workflow.set_entry_point("parser")

workflow.add_edge("parser", "evaluator")
workflow.add_edge("evaluator", "ai_detector")
workflow.add_edge("ai_detector", "scoring")
workflow.add_edge("scoring", "ranking")
workflow.add_edge("ranking", "decision")

graph = workflow.compile()