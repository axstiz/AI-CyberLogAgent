"""Type definitions for LangGraph compatibility."""

from typing import TypedDict, Optional, List, Any


class AnalysisState(TypedDict, total=False):
    """
    State type for LangGraph (future compatibility).

    This TypedDict defines the state that flows through the analysis pipeline.
    Currently used for type hints, will be used with LangGraph StateGraph.
    """

    # Input
    log_content: str

    # Agent 1 output
    primary_analysis: str
    events_found: int

    # RAG output
    mitre_context: str
    mitre_techniques: List[dict]
    technique_ids: List[str]
    search_query: str

    # Agent 2 output
    final_report: str
    severity_level_id: int
    threat_type_id: int
    mitre_techniques_final: List[str]

    # Metadata
    success: bool
    error: Optional[str]
    total_time_sec: float
    log_size: int


class PipelineResult(TypedDict, total=False):
    """Result type for pipeline execution."""

    success: bool
    log_size: int
    total_time_sec: float

    # Stage results
    agent1_result: Optional[dict]
    rag_result: Optional[dict]
    agent2_result: Optional[dict]

    # Error information
    error: Optional[str]
    error_stage: Optional[str]


class MITRATechnique(TypedDict):
    """MITRE ATT&CK technique type."""

    technique_id: str
    technique_name: str
    tactic: str
    description: str
    platforms: List[str]
    data_sources: List[str]
