using UnityEngine;
using UnityEngine.UI; // Use TMPro if using TextMeshPro
using System.Collections;
using TMPro;

public class TextDisplay : MonoBehaviour
{
    public TMP_Text descriptionText; // Use TMP_Text if using TextMeshPro
    public float displaySpeed = 0.05f;

    private string fullText;
    private Coroutine displayCoroutine;

    void Start()
    {
        // Example usage
        //SetText("This is an example description text that will be displayed chunk by chunk.");
    }

    public void SetText(string text)
    {
        fullText = text;
        if (displayCoroutine != null)
        {
            StopCoroutine(displayCoroutine);
        }
        displayCoroutine = StartCoroutine(DisplayText());
    }

    private IEnumerator DisplayText()
    {
        descriptionText.text = "";
        foreach (char c in fullText)
        {
            descriptionText.text += c;
            yield return new WaitForSeconds(displaySpeed);
        }
    }
}
