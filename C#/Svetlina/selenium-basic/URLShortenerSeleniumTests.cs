using System;
using System.Threading;
using NUnit.Framework;

using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTestsProject
{
    public class URLShortenerSeleniumTests
    {
        IWebDriver driver;

        [OneTimeSetUp]
        public void Setup()
        {
            this.driver = new ChromeDriver();
            //this.driver.Url = "https://en.wikipedia.org";
        }

        [Test]
        public void Test_HomePage_Valid()
        {
            this.driver.Url = "http://shorturl.nakov.repl.co/urls";
            string expectedTitle = "Short URLs";
            string expectedFirstRowOriginalUrl = "https://nakov.com";
            string expectedShortUrl = "http://shorturl.nakov.repl.co/go/nak";

            string title = this.driver.FindElement(By.CssSelector("main h1")).Text;
            IWebElement firstTableRow = this.driver.FindElement(By.CssSelector("tbody tr"));
            string firstRowOriginalUrl = firstTableRow.FindElement(By.CssSelector("td:nth-child(1)")).Text;
            string firstRowShortUrl = firstTableRow.FindElement(By.CssSelector("td:nth-child(2)")).Text;

            Assert.AreEqual(title, expectedTitle);
            Assert.AreEqual(firstRowOriginalUrl, expectedFirstRowOriginalUrl);
            Assert.AreEqual(firstRowShortUrl, expectedShortUrl);
        }

        [Test]
        public void Test_AddUrl_Valid()
        {
            // Arrange
            this.driver.Url = "https://shorturl.nakov.repl.co/add-url";
            string uniqueCode = DateTime.Now.Ticks.ToString();
            //IWebElement addUrlButton = this.driver.FindElement(By.LinkText("Add URL"));

            IWebElement urlTextField = this.driver.FindElement(By.Id("url"));
            IWebElement shortCodeTextField = this.driver.FindElement(By.Id("code"));
            IWebElement createButton = this.driver.FindElement(By.CssSelector("button"));

            urlTextField.Click();
            urlTextField.SendKeys("http://www.youtube.com/");

            shortCodeTextField.Click();
            shortCodeTextField.Clear();
            shortCodeTextField.SendKeys(uniqueCode);

            createButton.Click();

            IWebElement link = this.driver.FindElement(By.LinkText($"http://shorturl.nakov.repl.co/go/{uniqueCode}"));
            Assert.IsTrue(link.Displayed);
        }

        [Test]
        public void Test_AddUrl_Invalid()
        {
            this.driver.Url = "https://shorturl.nakov.repl.co/add-url";
            string expectedErrorMsg = "URL cannot be empty!";

            IWebElement urlTextField = this.driver.FindElement(By.Id("url"));
            urlTextField.Click();
            urlTextField.SendKeys("");

            IWebElement createButton = this.driver.FindElement(By.CssSelector("button"));
            createButton.Click();

            IWebElement errorMesageDiv = this.driver.FindElement(By.CssSelector(".err"));

            Assert.IsTrue(errorMesageDiv.Displayed);
            Assert.AreEqual(errorMesageDiv.Text, expectedErrorMsg);
        }

        [Test]
        public void Test_VisitUrl()
        {
            this.driver.Url = "https://shorturl.nakov.repl.co/urls";
            IWebElement firstTableRow  = this.driver.FindElement(By.CssSelector("tbody tr"));
            IWebElement urlLink = firstTableRow.FindElement(By.CssSelector("td:nth-child(2) a"));
           
            IWebElement visitsElement = firstTableRow.FindElement(By.CssSelector("td:last-child"));
            int visitsOriginal = int.Parse(visitsElement.Text);

            urlLink.Click();

            driver.SwitchTo().Window(driver.WindowHandles[1]);
            Thread.Sleep(2000);
            driver.SwitchTo().Window(driver.WindowHandles[0]);

            firstTableRow = this.driver.FindElement(By.CssSelector("tbody tr"));
            visitsElement = firstTableRow.FindElement(By.CssSelector("td:last-child"));
            int result = int.Parse(visitsElement.Text);

            Assert.That(visitsOriginal + 1, Is.EqualTo(result));
        }

        [OneTimeTearDown]
        public void TearDown()
        {
            //this.driver.Quit();
        }
    }
}
