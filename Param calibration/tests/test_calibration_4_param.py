
class test_cal_stats:
    def test_cal_stats(self):

        stats_result = cal_stats(n_real_return)

        #assert False

        self.assertEquals(
            stats_result.iloc[0, 0],
            np.mean(n_real_return.iloc[:, 0]))
        self.assertEquals(
            stats_result.iloc[0, 1],
            np.std(n_real_return.iloc[:, 0]))






from contacts.models import Contact  # import model Contact
...
class ContactTests(TestCase):  # start a test case
    """Contact model tests."""

    def test_str(self):  # start one test

        contact = Contact(first_name='John', last_name='Smith')  # create a Contact object with 2 params like that

        self.assertEquals(  # check if str(contact) == 'John Smith'
            str(contact),
            'John Smith',
        )