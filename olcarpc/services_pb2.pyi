# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from olca_pb2 import (
    Actor as olca_pb2___Actor,
    Category as olca_pb2___Category,
    Currency as olca_pb2___Currency,
    DQSystem as olca_pb2___DQSystem,
    Flow as olca_pb2___Flow,
    FlowMap as olca_pb2___FlowMap,
    FlowProperty as olca_pb2___FlowProperty,
    ImpactCategory as olca_pb2___ImpactCategory,
    ImpactMethod as olca_pb2___ImpactMethod,
    Location as olca_pb2___Location,
    ModelTypeValue as olca_pb2___ModelTypeValue,
    Parameter as olca_pb2___Parameter,
    Process as olca_pb2___Process,
    ProcessTypeValue as olca_pb2___ProcessTypeValue,
    ProductSystem as olca_pb2___ProductSystem,
    Project as olca_pb2___Project,
    Ref as olca_pb2___Ref,
    SocialIndicator as olca_pb2___SocialIndicator,
    Source as olca_pb2___Source,
    UnitGroup as olca_pb2___UnitGroup,
)

from typing import (
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Empty(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___Empty = Empty

class Status(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok"]) -> None: ...
type___Status = Status

class RefStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def ref(self) -> olca_pb2___Ref: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        ref : typing___Optional[olca_pb2___Ref] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"ref",b"ref"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"ref",b"ref"]) -> None: ...
type___RefStatus = RefStatus

class ActorStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def actor(self) -> olca_pb2___Actor: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        actor : typing___Optional[olca_pb2___Actor] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"actor",b"actor"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actor",b"actor",u"error",b"error",u"ok",b"ok"]) -> None: ...
type___ActorStatus = ActorStatus

class CategoryStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def category(self) -> olca_pb2___Category: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        category : typing___Optional[olca_pb2___Category] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"category",b"category"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"error",b"error",u"ok",b"ok"]) -> None: ...
type___CategoryStatus = CategoryStatus

class CurrencyStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def currency(self) -> olca_pb2___Currency: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        currency : typing___Optional[olca_pb2___Currency] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"currency",b"currency"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"currency",b"currency",u"error",b"error",u"ok",b"ok"]) -> None: ...
type___CurrencyStatus = CurrencyStatus

class DQSystemStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def dq_system(self) -> olca_pb2___DQSystem: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        dq_system : typing___Optional[olca_pb2___DQSystem] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dq_system",b"dq_system"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dq_system",b"dq_system",u"error",b"error",u"ok",b"ok"]) -> None: ...
type___DQSystemStatus = DQSystemStatus

class FlowStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def flow(self) -> olca_pb2___Flow: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        flow : typing___Optional[olca_pb2___Flow] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"flow",b"flow"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"flow",b"flow",u"ok",b"ok"]) -> None: ...
type___FlowStatus = FlowStatus

class FlowPropertyStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def flow_property(self) -> olca_pb2___FlowProperty: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        flow_property : typing___Optional[olca_pb2___FlowProperty] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"flow_property",b"flow_property"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"flow_property",b"flow_property",u"ok",b"ok"]) -> None: ...
type___FlowPropertyStatus = FlowPropertyStatus

class ImpactCategoryStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def impact_category(self) -> olca_pb2___ImpactCategory: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        impact_category : typing___Optional[olca_pb2___ImpactCategory] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"impact_category",b"impact_category"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"impact_category",b"impact_category",u"ok",b"ok"]) -> None: ...
type___ImpactCategoryStatus = ImpactCategoryStatus

class ImpactMethodStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def impact_method(self) -> olca_pb2___ImpactMethod: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        impact_method : typing___Optional[olca_pb2___ImpactMethod] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"impact_method",b"impact_method"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"impact_method",b"impact_method",u"ok",b"ok"]) -> None: ...
type___ImpactMethodStatus = ImpactMethodStatus

class LocationStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def location(self) -> olca_pb2___Location: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        location : typing___Optional[olca_pb2___Location] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"location",b"location"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"location",b"location",u"ok",b"ok"]) -> None: ...
type___LocationStatus = LocationStatus

class ParameterStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def parameter(self) -> olca_pb2___Parameter: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        parameter : typing___Optional[olca_pb2___Parameter] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"parameter",b"parameter"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"parameter",b"parameter"]) -> None: ...
type___ParameterStatus = ParameterStatus

class ProcessStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def process(self) -> olca_pb2___Process: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        process : typing___Optional[olca_pb2___Process] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"process",b"process"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"process",b"process"]) -> None: ...
type___ProcessStatus = ProcessStatus

class ProductSystemStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def product_system(self) -> olca_pb2___ProductSystem: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        product_system : typing___Optional[olca_pb2___ProductSystem] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"product_system",b"product_system"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"product_system",b"product_system"]) -> None: ...
type___ProductSystemStatus = ProductSystemStatus

class ProjectStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def project(self) -> olca_pb2___Project: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        project : typing___Optional[olca_pb2___Project] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"project",b"project"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"project",b"project"]) -> None: ...
type___ProjectStatus = ProjectStatus

class SocialIndicatorStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def social_indicator(self) -> olca_pb2___SocialIndicator: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        social_indicator : typing___Optional[olca_pb2___SocialIndicator] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"social_indicator",b"social_indicator"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"social_indicator",b"social_indicator"]) -> None: ...
type___SocialIndicatorStatus = SocialIndicatorStatus

class SourceStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def source(self) -> olca_pb2___Source: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        source : typing___Optional[olca_pb2___Source] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"source",b"source"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"source",b"source"]) -> None: ...
type___SourceStatus = SourceStatus

class UnitGroupStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def unit_group(self) -> olca_pb2___UnitGroup: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        unit_group : typing___Optional[olca_pb2___UnitGroup] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"unit_group",b"unit_group"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"unit_group",b"unit_group"]) -> None: ...
type___UnitGroupStatus = UnitGroupStatus

class DescriptorRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: olca_pb2___ModelTypeValue = ...
    id: typing___Text = ...
    name: typing___Text = ...
    category: typing___Text = ...

    def __init__(self,
        *,
        type : typing___Optional[olca_pb2___ModelTypeValue] = None,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"id",b"id",u"name",b"name",u"type",b"type"]) -> None: ...
type___DescriptorRequest = DescriptorRequest

class SearchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: olca_pb2___ModelTypeValue = ...
    query: typing___Text = ...

    def __init__(self,
        *,
        type : typing___Optional[olca_pb2___ModelTypeValue] = None,
        query : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"query",b"query",u"type",b"type"]) -> None: ...
type___SearchRequest = SearchRequest

class CreateSystemRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DefaultProvidersValue = typing___NewType('DefaultProvidersValue', builtin___int)
    type___DefaultProvidersValue = DefaultProvidersValue
    DefaultProviders: _DefaultProviders
    class _DefaultProviders(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[CreateSystemRequest.DefaultProvidersValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        Prefer = typing___cast(CreateSystemRequest.DefaultProvidersValue, 0)
        Ignore = typing___cast(CreateSystemRequest.DefaultProvidersValue, 1)
        Only = typing___cast(CreateSystemRequest.DefaultProvidersValue, 2)
    Prefer = typing___cast(CreateSystemRequest.DefaultProvidersValue, 0)
    Ignore = typing___cast(CreateSystemRequest.DefaultProvidersValue, 1)
    Only = typing___cast(CreateSystemRequest.DefaultProvidersValue, 2)
    type___DefaultProviders = DefaultProviders

    default_providers: type___CreateSystemRequest.DefaultProvidersValue = ...
    preferred_type: olca_pb2___ProcessTypeValue = ...

    @property
    def process(self) -> olca_pb2___Ref: ...

    def __init__(self,
        *,
        process : typing___Optional[olca_pb2___Ref] = None,
        default_providers : typing___Optional[type___CreateSystemRequest.DefaultProvidersValue] = None,
        preferred_type : typing___Optional[olca_pb2___ProcessTypeValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"process",b"process"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"default_providers",b"default_providers",u"preferred_type",b"preferred_type",u"process",b"process"]) -> None: ...
type___CreateSystemRequest = CreateSystemRequest

class FlowMapStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def flow_map(self) -> olca_pb2___FlowMap: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        flow_map : typing___Optional[olca_pb2___FlowMap] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"flow_map",b"flow_map"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"flow_map",b"flow_map",u"ok",b"ok"]) -> None: ...
type___FlowMapStatus = FlowMapStatus

class FlowMapInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...
type___FlowMapInfo = FlowMapInfo

class Result(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> None: ...
type___Result = Result

class ResultStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ok: builtin___bool = ...
    error: typing___Text = ...

    @property
    def result(self) -> type___Result: ...

    def __init__(self,
        *,
        ok : typing___Optional[builtin___bool] = None,
        result : typing___Optional[type___Result] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"ok",b"ok",u"result",b"result"]) -> None: ...
type___ResultStatus = ResultStatus
