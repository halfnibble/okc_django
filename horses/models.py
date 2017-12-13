from django.db import models


class Horse(models.Model):
    """
    Store details about horses for trade.
    """
    Arabian = 'Arabian'
    QuarterHorse = 'Quarter Horse'
    Thoroughbred = 'Thoroughbred'
    Appaloosa = 'Appaloosa'

    BREEDS = (
        (Arabian, Arabian),
        (QuarterHorse, QuarterHorse),
        (Thoroughbred, Thoroughbred),
        (Appaloosa, Appaloosa),
    )

    name = models.CharField('Name', max_length=255)
    breed = models.CharField(
        'Breed',
        max_length=255,
        choices=BREEDS,
        default=Arabian)
    listing_date = models.DateTimeField('Listing Date', auto_now_add=True)
    price = models.DecimalField(
        'Price',
        max_digits=8,
        decimal_places=2,
        default='0.00')

    def __unicode__(self):
        return '{0}, {1}, ${2}'.format(self.name, self.get_breed_display,
                                       self.price)

