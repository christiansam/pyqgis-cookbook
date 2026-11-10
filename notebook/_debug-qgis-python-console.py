# Python Console
# Use iface to access QGIS API interface or type '?' for more info
# Security warning: typing commands from an untrusted source can harm your computer
from qgis.core import (
    QgsApplication,
    QgsDataSourceUri,
    QgsCategorizedSymbolRenderer,
    QgsClassificationRange,
    QgsPointXY,
    QgsProject,
    QgsExpression,
    QgsField,
    QgsFields,
    QgsFeature,
    QgsFeatureRequest,
    QgsFeatureRenderer,
    QgsGeometry,
    QgsGraduatedSymbolRenderer,
    QgsMarkerSymbol,
    QgsMessageLog,
    QgsRectangle,
    QgsRendererCategory,
    QgsRendererRange,
    QgsSymbol,
    QgsVectorDataProvider,
    QgsVectorLayer,
    QgsVectorFileWriter,
    QgsWkbTypes,
    QgsSpatialIndex,
    QgsVectorLayerUtils,
)
from qgis.core.additions.edit import edit
from qgis.PyQt.QtGui import (
    QColor,
)

import os;
os.chdir("/home/sac0001/workspace/cicd/misc/pyqgis-cookbook/notebook")
print(os.getcwd())

vlayer = QgsVectorLayer(
    "testdata/data/data.gpkg|layername=airports", "Airports layer", "ogr"
)
for field in vlayer.fields():
    print(field.name(), field.typeName())
