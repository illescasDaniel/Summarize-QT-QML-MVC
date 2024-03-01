import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Popup {
	id: loadingPopup
	visible: false
	modal: true
	focus: true
	padding: 8
	closePolicy: Popup.NoAutoClose
	x: (window.width - loadingPopup.width) / 2
	y: (window.height - loadingPopup.height) / 2

	ColumnLayout {
		anchors.centerIn: parent
		spacing: 10

		BusyIndicator {
			Layout.alignment: Qt.AlignHCenter
		}

		Label {
			Layout.alignment: Qt.AlignHCenter
			text: "Processing..."
		}
	}
}
