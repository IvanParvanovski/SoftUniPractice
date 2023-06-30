using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;

namespace P04_FightingArena
{
    public class ArenaTests
    {
        private Arena arena;
        private List<Warrior> warriors;
        
        [SetUp]
        public void Setup()
        {
            arena = new Arena();
            warriors = new List<Warrior>
            {
                new Warrior("Achilles", 120, 240),
                new Warrior("Hector", 130, 260),
                new Warrior("Thor", 180, 360)
            };
        }

        [Test]
        public void CheckCollection()
        {
            EnrollDefaultWarriors();
            CollectionAssert.AreEqual(warriors, arena.Warriors);
        }

        [Test]
        public void TestEnrollWhenValid()
        {
            EnrollDefaultWarriors();
            Assert.AreEqual(3, arena.Count);
        }

        [TestCase("Achilles", 499, 781)]
        [TestCase("Hector", 888, 292)]
        [TestCase("Thor", 1282, 999)]
        public void TestEnrollShouldThrowInvalidOperationWhenInvalid
            (string name, int damage, int hp)
        {
            EnrollDefaultWarriors();

            var warrior = new Warrior(name, damage, hp);

            Assert.Throws<InvalidOperationException>(
                () => { arena.Enroll(warrior); }
            );
        }

        [Test]
        public void TestAttack()
        {
            this.EnrollDefaultWarriors();
            
            var attacker = arena.Warriors.First(w => w.Name == "Achilles");
            var defender = arena.Warriors.First(w => w.Name == "Hector");

            var expectedHp = defender.HP - attacker.Damage;

            if (expectedHp < 0) { expectedHp = 0; }

            arena.Fight("Achilles", "Hector");
            Assert.AreEqual(expectedHp, defender.HP);

        }

        [TestCase(null, "Hector")]
        [TestCase("Achilles", null)]

        public void FightThrowExceptionWhenInvalid(string attacker, string defender)
        {
            EnrollDefaultWarriors();
            
            Assert.Throws<InvalidOperationException>(
                () => { arena.Fight(attacker, defender);}
            );
        }

        private void EnrollDefaultWarriors()
        {
            foreach (var warrior in this.warriors)
            {
                arena.Enroll(warrior);
            }
        }

    }
}
