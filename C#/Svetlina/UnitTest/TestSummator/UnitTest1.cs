using Microsoft.VisualStudio.TestPlatform.TestHost;
using NUnit.Framework;


namespace TestSummator
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
            var sum = Program.Sum();
            Assert.Pass();
        }
    }
}