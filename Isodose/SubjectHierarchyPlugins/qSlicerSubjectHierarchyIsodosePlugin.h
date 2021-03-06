/*==============================================================================

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

==============================================================================*/

#ifndef __qSlicerSubjectHierarchyIsodosePlugin_h
#define __qSlicerSubjectHierarchyIsodosePlugin_h

// SlicerRt includes
#include "qSlicerSubjectHierarchyAbstractPlugin.h"

#include "qSlicerIsodoseSubjectHierarchyPluginsExport.h"

class qSlicerSubjectHierarchyIsodosePluginPrivate;
class vtkMRMLNode;
class vtkMRMLSubjectHierarchyNode;

/// \ingroup SlicerRt_QtModules_RtHierarchy
class Q_SLICER_ISODOSE_SUBJECT_HIERARCHY_PLUGINS_EXPORT qSlicerSubjectHierarchyIsodosePlugin : public qSlicerSubjectHierarchyAbstractPlugin
{
public:
  Q_OBJECT

public:
  typedef qSlicerSubjectHierarchyAbstractPlugin Superclass;
  qSlicerSubjectHierarchyIsodosePlugin(QObject* parent = NULL);
  virtual ~qSlicerSubjectHierarchyIsodosePlugin();

public:
  /// Determines if the actual plugin can handle a subject hierarchy item. The plugin with
  /// the highest confidence number will "own" the item in the subject hierarchy (set icon, tooltip,
  /// set context menu etc.)
  /// \param item Item to handle in the subject hierarchy tree
  /// \return Floating point confidence number between 0 and 1, where 0 means that the plugin cannot handle the
  ///   item, and 1 means that the plugin is the only one that can handle the item (by node type or identifier attribute)
  virtual double canOwnSubjectHierarchyItem(vtkIdType itemID)const;

  /// Get role that the plugin assigns to the subject hierarchy item.
  ///   Each plugin should provide only one role.
  Q_INVOKABLE virtual const QString roleForPlugin()const;

  /// Get icon of an owned subject hierarchy item
  /// \return Icon to set, empty icon if nothing to set
  virtual QIcon icon(vtkIdType itemID);

  /// Get visibility icon for a visibility state
  Q_INVOKABLE virtual QIcon visibilityIcon(int visible);

  /// Open module belonging to item and set inputs in opened module
  Q_INVOKABLE virtual void editProperties(vtkIdType itemID);

  /// Set display color of an owned subject hierarchy item
  /// \param color Display color to set
  /// \param terminologyMetaData Map containing terminology meta data
  virtual void setDisplayColor(vtkIdType itemID, QColor color, QMap<int, QVariant> terminologyMetaData);

  /// Get display color of an owned subject hierarchy item
  /// \param terminologyMetaData Output map containing terminology meta data
  virtual QColor getDisplayColor(vtkIdType itemID, QMap<int, QVariant> &terminologyMetaData)const;

protected:
  QScopedPointer<qSlicerSubjectHierarchyIsodosePluginPrivate> d_ptr;

private:
  Q_DECLARE_PRIVATE(qSlicerSubjectHierarchyIsodosePlugin);
  Q_DISABLE_COPY(qSlicerSubjectHierarchyIsodosePlugin);
};

#endif
