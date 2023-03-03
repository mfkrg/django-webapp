from django.test import TestCase
from .models import Image
from django.core.files import File


class GalleryModelTest(TestCase):
    def test_gallery_model_save_and_retrieve(self):
        image1 = Image(
            title='Title 1',
            image=File(open('gallery/test_images/iphone_xr.jpg', 'rb'))
        )
        image1.save()

        image2 = Image(
            title='Title 2',
            image=File(open('gallery/test_images/iphone_x.jpg', 'rb'))
        )
        image2.save()

        image3 = Image(
            title='Title 3',
            image=File(open('gallery/test_images/iphone_x.jpg', 'rb'))
        )
        image3.save()

        all_images = Image.objects.all()

        #counttest
        self.assertEqual(len(all_images), 3)

        #first one
        self.assertEqual(
            all_images[0].title, image1.title
        )

        self.assertEqual(
            all_images[0].image, image1.image
        )

        #second one
        self.assertEqual(
            all_images[1].title, image2.title
        )

        self.assertEqual(
            all_images[1].image, image2.image
        )

        #third one
        self.assertEqual(
            all_images[2].title, image3.title
        )

        self.assertEqual(
            all_images[2].image, image3.image
        )