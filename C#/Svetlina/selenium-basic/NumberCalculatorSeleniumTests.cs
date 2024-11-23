using NUnit.Framework;

using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTestsProject
{
    public class NumberCalculatorSeleniumTests
    {
        [OneTimeSetUp]
        public void Setup()
        {
        }

        // Valid Integers
        // Infinity
        // Invalid Inputs
        // Invalid Operators
        public void Test_CalculatorWebApp(string num1,
                                          string op,
                                          string num2,
                                          string expected)
        {
        }

        [OneTimeTearDown]
        public void TearDown()
        {
        }
    }
}
