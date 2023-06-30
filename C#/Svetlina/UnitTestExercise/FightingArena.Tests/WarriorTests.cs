using NUnit.Framework;
using System;
using System.Threading;

namespace P04_FightingArena
{
    public class WarriorTests
    {
        [Test]
        public void TestConstructorIfWorksCorrectly()
        {

            Warrior warrior = new Warrior("Random", 10, 100);
            
            Assert.AreEqual("Random", warrior.Name);
            Assert.AreEqual(10, warrior.Damage);
            Assert.AreEqual(100, warrior.HP);
        }

        [Test]
        public void TestNameValidatorWithNullName()
        {
            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior(null, 10, 100); }
            );
        }

        [Test]
        public void TestNameValidatorWithEmptyName()
        {
            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior(string.Empty, 10, 100);
            });
        }

        [Test]
        public void TestNameValidatorWithWhitespaceName()
        {
            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior(" ", 10, 100); }
            );
        }

        [Test]
        public void TestDamageValidatorWithZeroDamage()
        {
            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior("Random", 0, 100); }
            );
        }

        [Test]
        public void TestDamageValidatorWithNegativeDamage()
        {

            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior("Random", -1, 100); }
            );
        }

        [Test]
        public void TestHPValidatorWithNegativeHp()
        {
           
            Assert.Throws<ArgumentException>(
                () => { Warrior warrior = new Warrior("Random", 10, -1); }
            );
        }

        [Test]
        [TestCase(25)]
        [TestCase(30)]
        public void TestAttackerAttacksWithHPLowerThanOrEqual30ShouldThrowException(int attackerHP)
        {
            string attackerName = "Random";
            int attackerDamage = 10;
            
            string defenderName = "RandomRandom";
            int defenderDamage = 10;
            int defenderHP = 40;
            
            Warrior attacker = new Warrior(attackerName, attackerDamage, attackerHP);
            Warrior defender = new Warrior(defenderName, defenderDamage, defenderHP);
            
            Assert.Throws<InvalidOperationException>(() => { attacker.Attack(defender); });
        }

        [Test]
        [TestCase(25)]
        [TestCase(30)]
        public void TestDefenderDefendsWithHPLowerThanOrEqual30ShouldThrowException(int defenderHP)
        {
            Warrior attacker = new Warrior("Random", 10, 50);
            Warrior defender = new Warrior("RandomRandom", 10, defenderHP);
            
            Assert.Throws<InvalidOperationException>(() => { attacker.Attack(defender); });
        }

        [Test]
        public void TestWeakerAttackerAttacksStrongerDefenderShouldThrowException()
        {
            Warrior attacker = new Warrior("Random", 104, 40);
            Warrior defender = new Warrior("RandomRandom", 80, 40);
            
            Assert.Throws<InvalidOperationException>(() => { attacker.Attack(defender); });
        }

        [Test]
        public void TestAttackerDefenderHPShouldBeDecreasedBySuccessfullAttack()
        {
            int attackerDamage = 100;
            int attackerHP = 500;
            Warrior attacker = new Warrior("Random", attackerDamage, attackerHP);

            int defenderDamage = 100;
            int defenderHP = 500;
            Warrior defender = new Warrior("RandomRandom", defenderDamage, defenderHP);
            
            int expectedAttackerHP = attackerHP - defenderDamage;
            int expectedDefenderHP = defenderHP - attackerDamage;
            attacker.Attack(defender);
            
            Assert.AreEqual(expectedAttackerHP, attacker.HP);
            Assert.AreEqual(expectedDefenderHP, defender.HP);
        }

        [Test]
        public void TestStrongerAttackerShouldKillWeakerDefender()
        {
            Warrior attacker = new Warrior("Kesho", 60, 50);
            Warrior defender = new Warrior("Gosho", 10, 50);

            int expectedDefenderHP = 0;
            int expectedAttackerHP = attacker.HP - defender.Damage;
            attacker.Attack(defender);
            
            Assert.AreEqual(expectedAttackerHP, attacker.HP);
            Assert.AreEqual(expectedDefenderHP, defender.HP);
        }
    }
}
