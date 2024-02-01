from __future__ import annotations

from typing import Final

from localstack.aws.api.stepfunctions import InspectionData
from localstack.services.stepfunctions.asl.eval.aws_execution_details import AWSExecutionDetails
from localstack.services.stepfunctions.asl.eval.contextobject.contex_object import (
    ContextObjectInitData,
)
from localstack.services.stepfunctions.asl.eval.environment import Environment
from localstack.services.stepfunctions.asl.eval.event.event_history import EventHistoryContext


class TestStateEnvironment(Environment):
    inspection_data: Final[InspectionData]

    def __init__(
        self,
        aws_execution_details: AWSExecutionDetails,
        context_object_init: ContextObjectInitData,
        event_history_context: EventHistoryContext,
    ):
        super().__init__(
            aws_execution_details=aws_execution_details,
            context_object_init=context_object_init,
            event_history_context=event_history_context,
        )
        self.inspection_data = InspectionData()

    @classmethod
    def as_frame_of(
        cls, env: TestStateEnvironment, event_history_frame_cache: EventHistoryContext
    ) -> TestStateEnvironment:
        frame = super().as_frame_of(env=env, event_history_frame_cache=event_history_frame_cache)
        frame.inspection_data = env.inspection_data
        return frame
