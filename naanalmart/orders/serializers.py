from rest_framework import serializers
from orders.models import Orders, Packages



class PackageSerializer(serializers.ModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	#variation_set = VariationSerializer(many=True)
	#image = serializers.SerializerMethodField()
	#package = serializers.PrimaryKeyRelatedField(queryset=Orders.objects.all(), required=False)
	class Meta:
		model = Packages
		fields = [
			"package_id",
			"order",
			"name",
			"number",
			"quantity",
			"length",
			"breadth",
			"height",
			"width",
			#"variation_set",
		]




class OrderSerializer(serializers.ModelSerializer):
	order = PackageSerializer(many=True)
	class Meta:
		model = Orders
		fields = ('order_id','order')

	# def create(self, validated_data):
	# 	package_data = validated_data.pop('order')
	# 	album = Orders.objects.create(**validated_data)
	# 	for track_data in package_data:
	# 		Packages.objects.create(album=album, **track_data)
	# 	return album


# class CategorySerializer(serializers.ModelSerializer):
# 	url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
# 	product_set = ProductSerializer(many=True)
# 	class Meta:
# 		model = Category
# 		fields = [
# 			"url",
# 			"id",
# 			"title",
# 			"description",
# 			"product_set",


# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ('order', 'title', 'duration')

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True)

#     class Meta:
#         model = Album
#         fields = ('album_name', 'artist', 'tracks')

#     def create(self, validated_data):
#         tracks_data = validated_data.pop('tracks')
#         album = Album.objects.create(**validated_data)
#         for track_data in tracks_data:
#             Track.objects.create(album=album, **track_data)
#         return album