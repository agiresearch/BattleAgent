using UnityEngine;
using UnityEngine.UI; // Use TMPro if using TextMeshPro
using System.Collections;
using TMPro;

public class TextDisplay : MonoBehaviour
{
    public TMP_Text descriptionText; // Use TMP_Text if using TextMeshPro
    public float displaySpeed = 0.05f;
    public AudioClip typeSound;

    [SerializeField] private AudioSource audioSource;
    private string fullText;
    private Coroutine displayCoroutine;

    void Start()
    {

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
        //PlayTypeSound();

        audioSource.loop = true;
        audioSource.clip = typeSound;
        audioSource.pitch = 5f;
        audioSource.Play();

        foreach (char c in fullText)
        {
            descriptionText.text += c;
            yield return new WaitForSeconds(displaySpeed);
        }

        audioSource.Stop();
        audioSource.loop = false;
    }


}
