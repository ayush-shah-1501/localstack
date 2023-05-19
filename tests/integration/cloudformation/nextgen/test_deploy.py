from typing import TypeVar

import pytest

from localstack.services.opensearch.cfn_resources import OpenSearchServiceDomainAllProperties
from localstack.services.ssm.cfn_resources import SSMParameterAllProperties
from localstack.utils.strings import short_uid

Properties = TypeVar("Properties")


@pytest.mark.parametrize(
    "type_name,props",
    [
        (
            "AWS::OpenSearchService::Domain",
            OpenSearchServiceDomainAllProperties(DomainName=f"domain-{short_uid()}"),
        ),
        (
            "AWS::SSM::Parameter",
            SSMParameterAllProperties(Type="String", Value=f"value-{short_uid()}"),
        ),
    ],
    ids=["opensearch-domain", "ssm-parameter"],
)
@pytest.mark.skip(reason="Example")
def test_roundtrip(type_name, props, perform_cfn_operation, aws_client):
    # deploy
    event = perform_cfn_operation(
        logical_resource_id="MyResource",
        resource_type=type_name,
        action="Add",
        resource_props=props,
    )

    # delete
    perform_cfn_operation(
        logical_resource_id="MyResource",
        resource_type=type_name,
        action="Remove",
        resource_props=event.resource_model,
    )