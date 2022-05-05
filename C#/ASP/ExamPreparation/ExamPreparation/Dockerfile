FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["ExamPreparation/ExamPreparation.csproj", "ExamPreparation/"]
RUN dotnet restore "ExamPreparation/ExamPreparation.csproj"
COPY . .
WORKDIR "/src/ExamPreparation"
RUN dotnet build "ExamPreparation.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ExamPreparation.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ExamPreparation.dll"]
