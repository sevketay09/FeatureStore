# Importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
    ValueType
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64,Int32 ,Int64
from datetime import timedelta

# Declaring an entity for the dataset
patient = Entity(
    name="patient", 
    value_type= ValueType.INT64, 
    join_keys= ["patient_id"],
    description="The ID of the patient")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r"/home/sevket/feast/breast_cancer/data/data_df1.parquet",
    timestamp_field="event_timestamp" # oluşturduğum timestamp column ismini verdim
)

#/home/sevket/feast/breast_cancer/data/data_df1.parquet

# Defining the first set of features

'''
Feast, çıkarım amacıyla modele yalnızca yeni özelliklerin sunulmasını sağlamak için ttl'yi kullanır.

schmea : Özellik görünümüne dahil etmek istediğimiz özellikler
source : özelliklerin kaynağı

'''
df1_fv = FeatureView(
    name="df1_feature_view", # feature view ismi
    ttl=timedelta(seconds=86400 * 3), # feature viewdeki özelliklerin ön belleğe alınması gereken süre
    entities=[patient],
    schema=[
        Field(name="mean radius", dtype=Float32),
        Field(name="mean texture", dtype=Float32),
        Field(name="mean perimeter", dtype=Float32),
        Field(name="mean area", dtype=Float32),
        Field(name="mean smoothness", dtype=Float32)
        ],
    online=True,    
    source=f_source1
)

# Declaring the source of the second set of features
f_source2 = FileSource(
    path=r"/home/sevket/feast/breast_cancer/data/data_df2.parquet",
    timestamp_field="event_timestamp"
)

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities= [patient],
    schema=[
        Field(name="mean compactness", dtype=Float32),
        Field(name="mean concavity", dtype=Float32),
        Field(name="mean concave points", dtype=Float32),
        Field(name="mean symmetry", dtype=Float32),
        Field(name="mean fractal dimension", dtype=Float32)
        ],  
    online=True, 
    source=f_source2
)

# Declaring the source of the third set of features
f_source3 = FileSource(
    path=r"/home/sevket/feast/breast_cancer/data/data_df3.parquet",
    timestamp_field="event_timestamp"
)

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities= [patient],
    schema=[
        Field(name="radius error", dtype=Float32),
        Field(name="texture error", dtype=Float32),
        Field(name="perimeter error", dtype=Float32),
        Field(name="area error", dtype=Float32),
        Field(name="smoothness error", dtype=Float32),
        Field(name="compactness error", dtype=Float32),
        Field(name="concavity error", dtype=Float32)
        ], 
    online=True,   
    source=f_source3
)

# Declaring the source of the fourth set of features
f_source4 = FileSource(
    path=r"/home/sevket/feast/breast_cancer/data/data_df4.parquet",
    timestamp_field="event_timestamp"
)

# Defining the fourth set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities= [patient],
    schema=[
        Field(name="concave points error", dtype=Float32),
        Field(name="symmetry error", dtype=Float32),
        Field(name="fractal dimension error", dtype=Float32),
        Field(name="worst radius", dtype=Float32),
        Field(name="worst texture", dtype=Float32),
        Field(name="worst perimeter", dtype=Float32),
        Field(name="worst area", dtype=Float32),
        Field(name="worst smoothness", dtype=Float32),
        Field(name="worst compactness", dtype=Float32),
        Field(name="worst concavity", dtype=Float32),
        Field(name="worst concave points", dtype=Float32),
        Field(name="worst symmetry", dtype=Float32),
        Field(name="worst fractal dimension", dtype=Float32),        
        ],  
    online=True,  
    source=f_source4
)

# Declaring the source of the targets
target_source = FileSource(
    path=r"/home/sevket/feast/breast_cancer/data/target_df.parquet", 
    timestamp_field="event_timestamp"
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities= [patient],
    ttl=timedelta(seconds=86400 * 3),
    schema=[
        Field(name="target", dtype=Int32)        
        ],  
    online=True,  
    source=target_source
)