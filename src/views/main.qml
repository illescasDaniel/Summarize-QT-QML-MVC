import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
	id: window
	visible: true
	width: 800
	height: 600
	title: "Text Summarizer"

	ColumnLayout {
		spacing: 10
		anchors.fill: parent

		ScrollView {
			Layout.fillWidth: true
			Layout.fillHeight: true
			Layout.preferredHeight: parent.height * 0.4
			TextArea {
				id: inputText
				wrapMode: TextEdit.Wrap
				placeholderText: "Enter text to summarize..."
			}
		}

		Button {
			Layout.alignment: Qt.AlignHCenter
			id: summarizeButton
			text: "Summarize"
			onClicked: textSummaryController.summarize(inputText.text)
		}

		ScrollView {
			Layout.fillWidth: true
			Layout.fillHeight: true
			Layout.preferredHeight: parent.height * 0.4
			TextArea {
				id: outputText
				wrapMode: TextEdit.Wrap
				readOnly: true
				placeholderText: "Summarized text will appear here..."
			}
		}
	}

	Loader {
		id: popupLoader
		source: "LoadingPopup.qml"
		asynchronous: true
		// active: textSummaryController.isLoading
	}

	Connections {
		target: textSummaryController
		function onSummaryReady(summary) {
			outputText.text = summary
		}
		function onIsLoading(enabled) {
			summarizeButton.enabled = !enabled
			popupLoader.item.visible = enabled
		}
	}
}
